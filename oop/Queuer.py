class Queuer:
    def __init__(self, ticket=None, user=None) -> None:
        self.user = user
        self.ticket = ticket
        self.is_valid = False
        self.fine = 0