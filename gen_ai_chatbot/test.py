from gen_ai_chatbot.exception.exceptions import RoleBasedRagChatBot

def some_logic():
    try:
        raise ValueError("A test error occurred")
    except Exception as e:
        raise RoleBasedRagChatBot("Error inside some_logic", e)

if __name__ == "__main__":
    try:
        some_logic()
    except RoleBasedRagChatBot as err:
        print(err)  # 👈 This line prints your custom exception message

    