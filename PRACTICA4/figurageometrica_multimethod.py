'''
Calcular el área de diferentes figuras
geométricas usando el mismo nombre de método.
'''
from multimethod import multimethod
import math

class FiguraGeometrica:
    
    
    @multimethod
    def area(self, radio: float):
        return math.pi * radio**2

    
    @multimethod
    def area(self, base: float, altura: float):
        return base * altura

    
    @multimethod
    def area(self, base: float, altura: float, tipo: str):
        if tipo == "triangulo":
            return (base * altura) / 2
        raise ValueError("Tipo de figura desconocido")

    
    @multimethod
    def area(self, baseMayor: float, baseMenor: float, altura: float):
        return ((baseMayor + baseMenor) * altura) / 2


    @multimethod
    def area(self, lado: float, tipo: str):
        if tipo == "pentagono":
            apotema = lado / (2 * math.tan(math.pi / 5))
            perimetro = 5 * lado
            return (perimetro * apotema) / 2
        raise ValueError("Solo soporta pentágonos regulares")

figura = FiguraGeometrica()

print("Área del círculo:", figura.area(5.0))
print("Área del rectángulo:", figura.area(4.0, 6.0))
print("Área del triángulo:", figura.area(4.0, 6.0, "triangulo"))
print("Área del trapecio:", figura.area(6.0, 4.0, 5.0))
print("Área del pentágono:", figura.area(3.0, "pentagono"))
