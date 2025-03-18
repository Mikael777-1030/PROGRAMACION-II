class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Línea desde {self.p1} hasta {self.p2}"

    def dibujaLinea(self):
        print(f"Dibujando línea desde {self.p1} hasta {self.p2}")
