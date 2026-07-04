// Baked in at build time (Vite env vars are compile-time). Falls back to the
// same URL used in native local dev when not overridden.
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export async function askQuestion(query, k = 5) {
  const response = await fetch(`${API_BASE_URL}/ask`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, k }),
  })

  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`)
  }

  return response.json()
}

// Streams the answer as it is generated. `onChunk` is called with each text
// fragment as it arrives. Throws if the request fails outright or if the
// backend reports an error mid-stream (already-sent 200 status can't carry
// an HTTP error code at that point, so the pipeline reports it as an SSE
// {"error": "..."} event instead).
export async function askQuestionStream(query, k = 5, onChunk) {
  const response = await fetch(`${API_BASE_URL}/ask/stream`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, k }),
  })

  if (!response.ok || !response.body) {
    throw new Error(`Request failed with status ${response.status}`)
  }

  const reader = response.body.getReader()
  const decoder = new TextDecoder()
  let buffer = ''

  while (true) {
    const { done, value } = await reader.read()
    if (done) break

    buffer += decoder.decode(value, { stream: true })
    const events = buffer.split('\n\n')
    buffer = events.pop()

    for (const event of events) {
      const line = event.trim()
      if (!line.startsWith('data:')) continue

      const payload = JSON.parse(line.slice(5).trim())
      if (payload.error) {
        throw new Error(payload.error)
      }
      if (typeof payload.chunk === 'string') {
        onChunk(payload.chunk)
      }
    }
  }
}
