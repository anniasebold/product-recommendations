class OpenAIError(Exception):
    def __init__(self, message, error_type=None, code=None):
        self.message = message
        self.error_type = error_type
        self.code = code
        super().__init__(self.message)
