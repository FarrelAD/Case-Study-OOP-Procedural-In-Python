class DepartureGate:
    def __init__(self) -> None:
        self.is_open = False

    def open_gate(self):
        self.is_open = True

    def close_gate(self):
        self.is_open = False