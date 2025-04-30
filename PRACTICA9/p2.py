import random
from abc import ABC, abstractmethod

class Coloreado(ABC):
    @abstractmethod
    def como_colorear(self):
        pass

class Figura(ABC):
    def __init__(self, color):
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def como_colorear(self):
        return "Colorear los cuatro lados"

    def __str__(self):
        return f"Cuadrado - Lado: {self.lado}, {super().__str__()}"

class Circulo(Figura):
    def __init__(self, radio, color):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio

    def __str__(self):
        return f"Circulo - Radio: {self.radio}, {super().__str__()}"

def main():
    figuras = []
    colores = ["Rojo", "Verde", "Azul", "Amarillo", "Negro"]

    for _ in range(5):
        tipo = random.randint(1, 2)  
        color = random.choice(colores)

        if tipo == 1:
            lado = random.randint(1, 10)
            figura = Cuadrado(lado, color)
        else:
            radio = random.randint(1, 10)
            figura = Circulo(radio, color)

        figuras.append(figura)

    for figura in figuras:
        print(figura)
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")
        if isinstance(figura, Coloreado):
            print("Coloración:", figura.como_colorear())
        print("-" * 30)


if __name__ == "__main__":
    main()
