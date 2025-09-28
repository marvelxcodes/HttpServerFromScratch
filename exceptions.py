class UnauthorizedAccessException(Exception):
    def __init__(self, code = 401, message = 'Unauthorized access') -> None:
        self.message = message
        self.code = code

        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message

class InternalServerException(Exception):
    def __init__(self, code = 500, message = 'Internal server error') -> None:
        self.message = message
        self.code = code

        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message



def handle_exception():
    try:
        raise UnauthorizedAccessException()
    except UnauthorizedAccessException as err:
        print(err.code)

    except InternalServerException as err:
        print(err.code)

handle_exception()
