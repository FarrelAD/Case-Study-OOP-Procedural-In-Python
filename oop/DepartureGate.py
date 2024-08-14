class DepartureGate:
    def __init__(self, is_open) -> None:
        self.is_open = is_open
        
    def open_gate(self):
        self.is_open = True
        
    def close_gate(self):
        self.is_open = False