from typing import Literal

EMBEDDING_MODEL: str = "text-embedding-004"

SIMILARITY_SCORE_THRESHOLD: float = 0.3
RETRIEVAL_RESULTS: int = 5

TLM_PROMPT_QUALITY_PRESET: Literal["best", "high", "medium", "low", "base"] = "base"

EVAL_THRESHOLD_OVERRIDES: dict[str, float] = {
    "trustworthiness": 0.75,
    "response_helpfulness": 0.75,
    "context_sufficiency": 0,
    "response_groundedness": 0,
    "query_ease": 0,
}

SCORE_TO_ISSUE = {
    "trustworthiness": "Untrustworthy",
    "context_sufficiency": "Insufficient Context",
    "response_groundedness": "Ungrounded",
    "response_helpfulness": "Unhelpful",
    "politeness": "Frustration in Query",
}

PROMPT_TEMPLATE: str = """You are a customer support agent working at Anysphere, a company whose main product is Cursor, an AI IDE. You are tasked with answering questions from users about Cursor and its features. You have access to a set of documents that provide information about Cursor, and you will use this information to answer the user's question. Your goal is to provide helpful answers to the user's questions based on the provided context.

Remember to follow these instructions:

1. NEVER use phrases like "according to the context", "as the context states", etc. Treat the Context as your own knowledge, not something you are referencing.
2. Give a clear, short, and accurate answer. Explain complex terms if needed.

Use the following pieces of retrieved Context to answer the Question.

<Context>
{context}
</Context>

Please write a response to the following Question, using the above Context:

{question}
"""  # noqa: E501

RELATED_TO_COMPETITOR_CRITERIA: str = "Evaluate if the Question is related to a competitor of {company_name} in any way. Examples may include questions that ask about competitor features, services, or pricing and how they compare to {company_name}. Some of {company_name}'s competitors include {competitors}."  # noqa: E501
RELATED_TO_COMPETITOR_QUERY_IDENTIFIER: str = "Question"

QUERY_POLITENESS_CRITERIA: str = "Evaluate if the Question recieved by a customer support chatbot is polite. Questions that are NOT polite may include language that indicates frustration, anger, or dissatisfaction. In particular, questions with negative tone or language directed at {company_name} or their products/services should be considered NOT polite. You want to distinguish between questions that are polite and questions that are NOT polite because Questions that are polite indicate that the user is patient and it is less critical to provide a perfect answer while Questions that are NOT polite indicate that the user is frustrated and it is more critical to provide a perfect answer. It is CRITICAL for you to make this distinction so that we do not lose customers who are frustrated with the product."  # noqa: E501
QUERY_POLITENESS_QUERY_IDENTIFIER: str = "Question"
