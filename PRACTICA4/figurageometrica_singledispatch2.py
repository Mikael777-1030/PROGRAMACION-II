""" Utilizando clases personalizadas para cada figura """
from functools import singledispatchmethod
import math

# Definimos clases para cada figura
class Circulo:
    def __init__(self, radio):
        self.radio = radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

class Trapecio:
    def __init__(self, base_mayor, base_menor, altura):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

class PentagonoRegular:
    def __init__(self, lado):
        self.lado = lado

# Clase principal que calcula las áreas
class FiguraGeometrica:
    
    @singledispatchmethod
    def area(self, figura):
        raise ValueError("Figura no soportada")
    
    # Círculo
    @area.register
    def _(self, figura: Circulo):
        return math.pi * figura.radio**2

    # Rectángulo
    @area.register
    def _(self, figura: Rectangulo):
        return figura.base * figura.altura

    # Triángulo
    @area.register
    def _(self, figura: Triangulo):
        return (figura.base * figura.altura) / 2

    # Trapecio
    @area.register
    def _(self, figura: Trapecio):
        return ((figura.base_mayor + figura.base_menor) * figura.altura) / 2

    # Pentágono regular (se calcula el apotema)
    @area.register
    def _(self, figura: PentagonoRegular):
        apotema = figura.lado / (2 * math.tan(math.pi / 5))
        perimetro = 5 * figura.lado
        return (perimetro * apotema) / 2

figura = FiguraGeometrica()

print("Área del círculo:", figura.area(Circulo(5)))
print("Área del rectángulo:", figura.area(Rectangulo(4, 6)))
print("Área del triángulo:", figura.area(Triangulo(4, 6)))
print("Área del trapecio:", figura.area(Trapecio(6, 4, 5)))
print("Área del pentágono:", figura.area(PentagonoRegular(3)))
