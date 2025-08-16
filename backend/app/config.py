import os
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class Settings(BaseModel):
    app_name: str = "PizzaBot"
    env: str = os.getenv("ENV", "dev")
    port: int = int(os.getenv("PORT", 8000))
    host: str = os.getenv("HOST", "0.0.0.0")

    # LangSmith Opt-in
    langsmith_api_key: str | None = os.getenv("LANGSMITH_API_KEY")
    # langsmith_project: str | None = os.getenv("LANGSMITH_PROJECT", "pizzabot")
    # langsmith_tracing: bool = os.getenv("LANGSMITH_TRACING", "true").lower() == "true"

    # Gemini API Key (loaded from .env as GEMINI_API_KEY)
    gemini_api_key: str = Field(default_factory=lambda: os.getenv("GEMINI_API_KEY", ""))

    # Vector DB
    vectordb_dir: str = os.getenv("VECTORDB_DIR", "./data/chroma")

    # CORS
    frontend_origin: str = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")

settings = Settings()
