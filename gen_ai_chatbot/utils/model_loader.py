import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from configure.config_loader import load_config
from exception.exceptions import RoleBasedRagChatBot

class ModelLoader:
    """
    A utility class to load embedding models and LLM models.
    """
    def __init__(self):
        load_dotenv(override=True)
        self._validate_env()
        self.config = load_config()

    def _validate_env(self):
        """
        Validate necessary environment variables.
        """
        required_vars = ["GOOGLE_API_KEY"]
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        if missing_vars:
            raise RoleBasedRagChatBot(
                "Missing required environment variables",
                Exception(str(missing_vars))
            )

    def load_embeddings(self):
        """
        Load and return the Google Generative AI embedding model.
        """
        print("🔎 Loading Google Generative AI Embedding model...")
        model_name = self.config["embedding_model"]["model_name"]
        return GoogleGenerativeAIEmbeddings(model=model_name)

    def load_llm(self):
        """
        Load and return the Google Generative AI LLM model.
        """
        print("🧠 Loading Google Generative AI Chat Model...")
        model_name = self.config["llm"]["model_name"]
        return ChatGoogleGenerativeAI(model=model_name)
