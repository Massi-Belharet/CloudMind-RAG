"""
Prompts module 

Defines prompts used across the RAG pipeline

Functions:
    get_rag_prompt() -> ChatPromptTemplate : Return the main RAG prompt template.
    get_multi_query_prompt(n_queries: int) -> ChatPromptTemplate : Return the multi-query reformulation prompt template.
"""

from langchain_core.prompts import ChatPromptTemplate


RAG_SYSTEM_PROMPT = """You are CloudMind, an expert AI assistant specialized in cloud architecture, FinOps, and multi-cloud optimization.

Your role is to help users make informed decisions about their cloud infrastructure based on official documentation, best practices, and FinOps data.

## Rules
- Answer ONLY based on the provided context.
- If the answer is not in the context, say clearly that you cannot answer based on available documentation.
- Never hallucinate costs, metrics, or technical specifications.
- Always mention which provider (AWS, Azure, GCP) the information comes from when possible.
- Respond in the same language as the user's question (French or English).

## Response Format
- Start with a direct answer to the question.
- If recommending an action, make it concrete and actionable.
- Keep responses concise — avoid unnecessary repetition.

## Data Sensitivity
- Treat all FinOps cost data as confidential.
- Never expose raw cost figures without context.
- Always present costs with their time period and scope."""

RAG_HUMAN_PROMPT = """Context:
{context}

Question: {question}

Answer:"""


MULTI_QUERY_SYSTEM_PROMPT = """You are an AI assistant specialized in cloud FinOps and multi-cloud architecture.
Your task is to generate {n_queries} alternative versions of the user's question.

Each alternative must explore a DIFFERENT angle or aspect of the original question,
not just a surface-level paraphrase or synonym substitution. Vary:
- terminology (technical vs business language)
- sub-aspects of the topic
- level of specificity (broader or narrower framing)

Return ONLY the {n_queries} questions, one per line, with no numbering and no extra text."""

MULTI_QUERY_HUMAN_PROMPT = "Original question: {question}"


def get_rag_prompt() -> ChatPromptTemplate:
    """
    Return the main RAG prompt template for CloudMind.

    Returns:
        ChatPromptTemplate: LangChain prompt template with context and question variables.
    """
    return ChatPromptTemplate.from_messages([
        ("system", RAG_SYSTEM_PROMPT),
        ("human", RAG_HUMAN_PROMPT)
    ])


def get_multi_query_prompt(n_queries: int) -> ChatPromptTemplate:
    """
    Return the multi-query reformulation prompt template.

    Args:
        n_queries (int): Number of reformulations the LLM should generate.

    Returns:
        ChatPromptTemplate: Prompt template with the system message pre-filled
        with n_queries and a human message expecting a 'question' variable.
    """
    system = MULTI_QUERY_SYSTEM_PROMPT.format(n_queries=n_queries)
    return ChatPromptTemplate.from_messages([
        ("system", system),
        ("human", MULTI_QUERY_HUMAN_PROMPT)
    ])