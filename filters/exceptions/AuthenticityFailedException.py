
class AuthenticityFailedException(Exception):


    def __init__(self, message) -> None:
        self.message = message


    def printMessage(self):
        print(self.message)
