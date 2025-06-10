from setuptools import setup, find_packages
from typing import List


setup(
    name="role_based_rag_chatbot",
    version="0.1.0",
    description="RAG Chatbot with Role-Based Access Control",
    author="ds-rpc-01",
    packages=find_packages(where="gen_ai_chatbot"),
    package_dir={"": "gen_ai_chatbot"},
    install_requires=[
        "langchain_astradb",
        "langchain_google_genai",
        "fastapi",
        "uvicorn",
        "python-multipart",
        "jinja2",
        "python-dotenv",
        "langchain",
        "langchain_core",
        "langchain-openai",
        "langchain_community",
        "streamlit",
    ],
    python_requires=">=3.10",
)
