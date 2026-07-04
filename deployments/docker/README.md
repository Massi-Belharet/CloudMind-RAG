# CloudMind — Dockerized deployment

This is an **alternative** to the native local workflow (`uv run uvicorn ...`,
`npm run dev`) — it does not replace it. Both work independently.

## Prerequisites

- Docker Desktop with GPU passthrough enabled (verified via
  `deployments/docker/Dockerfile.gpu-test` — see below).
- Ollama running **natively on the host** (not containerized) with the
  required models pulled (`llama3.1:8b`, `llama3.2:1b`, ...). The backend
  container reaches it via `host.docker.internal`.
- A `.env` file at the repo root (copy `.env.example`) with `POSTGRES_*`,
  `LANGSMITH_*` values — `docker-compose.yml` reads it for the services below.

## GPU passthrough smoke test

Before touching the real backend image, `Dockerfile.gpu-test` verifies that
`torch.cuda.is_available()` works inside a container, using the exact CUDA
wheel index pinned in the root `pyproject.toml`
(`[tool.uv.sources]` / `[[tool.uv.index]]`, currently `cu124`):

```bash
docker build -f deployments/docker/Dockerfile.gpu-test -t cloudmind-gpu-test .
docker run --rm --gpus all cloudmind-gpu-test
```

Expected output: `CUDA available: True` and your GPU's name. If this fails,
do not proceed with the rest — check that Docker Desktop's GPU support is
enabled and that `docker info` lists an `nvidia` runtime.

## First-time setup — build the Qdrant index

`backend/src/api/build_index.py` is a **one-shot script**, not a container
entrypoint — the API never re-indexes on its own. Run it once against the
dockerized Qdrant, before starting the backend service for the first time
(or whenever the source corpus under `backend/data/raw/` changes):

```bash
docker compose build backend
docker compose up -d qdrant pgvector
docker compose run --rm backend uv run python backend/src/api/build_index.py
```

`docker compose run` reuses the backend service's GPU reservation, so this
gets GPU access the same way the API itself does.

## Running everything

```bash
docker compose up --build
```

This starts Qdrant, Pgvector, the backend API (GPU-enabled), and the frontend
(served via nginx). Wait for the backend logs to show:

```
Pipeline ready
```

Then open the frontend at `http://localhost:5173`.

## Platform note — `host.docker.internal`

The backend needs to reach Ollama on the host machine. `host.docker.internal`
works natively on **Docker Desktop (Windows, macOS)**. On **native Linux**
Docker Engine it is not available by default — `docker-compose.yml` already
includes the `extra_hosts: host.docker.internal:host-gateway` workaround,
which makes it resolve consistently on all three platforms. No changes
needed unless your Linux Docker version doesn't support `host-gateway`
(added in Docker 20.10+), in which case set `OLLAMA_HOST` directly to the
host's LAN/bridge IP instead.

## What's NOT containerized

- **Ollama** — runs natively on the host (GPU-heavy LLM serving, kept outside
  Docker deliberately per this project's setup).
- Local dev workflow (`uv run uvicorn ...`, `npm run dev`) still works exactly
  as before — this Docker setup doesn't change or depend on it.
