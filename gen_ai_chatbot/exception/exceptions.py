import sys

class RoleBasedRagChatBot(Exception):
    def __init__(self, error_message: str, error_detail: Exception):
        self.error_message = error_message
        _, _, exc_tb = sys.exc_info()
        self.lineno = exc_tb.tb_lineno if exc_tb else None
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        self.original_exception = error_detail

    def __str__(self):
        return (
            f"Error occurred in python script [{self.file_name}] "
            f"line [{self.lineno}] "
            f"error message [{self.error_message}] "
            f"original error: [{self.original_exception}]"
        )


# ✅ Test usage
if __name__ == '__main__':
    try:
        raise ValueError("An example error")
    except Exception as e:
        raise RoleBasedRagChatBot("Test run failed", e)  # ✅ Pass both arguments!
