from gen_ai_chatbot.utils.model_loader import ModelLoader
from gen_ai_chatbot.exception.exceptions import RoleBasedRagChatBot

def test_model_loading():
    try:
        loader = ModelLoader()
        embeddings = loader.load_embeddings()
        print("✅ Embeddings loaded:", type(embeddings))
        llm = loader.load_llm()
        print("✅ LLM loaded:", type(llm))

    except RoleBasedRagChatBot as e:
        print("❌ Custom Exception Triggered:")
        print(e)

    except Exception as e:
        print("❌ General Exception Triggered:")
        print(e)

if __name__ == "__main__":
    test_model_loading()
