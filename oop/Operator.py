import DepartureGate

class Operator:
    gate = DepartureGate()
    
    def __init__(self, name) -> None:
        self.name = name
    
    def open_departure_gate(self):
        self.gate.open_gate()
        
    def close_departure_gate(self):
        self.gate.close_gate()