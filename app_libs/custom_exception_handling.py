class ResponseError(Exception):
    def __init__(self, message, status_code=None, error_code=None, success_code=None, params=None):
        super().__init__(message)
        self.message = str(message)
        self.status_code = status_code
        self.error_code = error_code
        self.success_code = success_code
        self.params = params