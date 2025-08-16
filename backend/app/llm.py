import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.language_models.chat_models import BaseChatModel
from .config import settings

# LangSmith tracing optional
#if settings.langsmith_tracing and settings.langsmith_api_key:
    #os.environ["LANGCHAIN_TRACING_V2"] = "true"
    #os.environ["LANGCHAIN_PROJECT"] = settings.langsmith_project or "pizzabot"


def get_chat_model() -> BaseChatModel:
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        api_key=settings.gemini_api_key,
        temperature=0.3,
    )