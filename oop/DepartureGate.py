class DepartureGate:
    def __init__(self) -> None:
        self.is_open = False

    def open_gate(self):
        print('Gerbang keberangkatan telah dibuka!')
        self.is_open = True

    def close_gate(self):
        print('Gerbang keberangkatan ditutup! Dimohon para penumpang untuk sabar menunggu keberangkatan selanjutnya')
        self.is_open = False