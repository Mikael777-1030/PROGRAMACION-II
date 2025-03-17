""" Utilizando diccionarios """
from functools import singledispatchmethod
import math

class FiguraGeometrica:
    
    @singledispatchmethod
    def area(self, figura):
        raise ValueError("Figura no soportada")
    
    # Círculo: {'tipo': 'circulo', 'radio': valor}
    @area.register
    def _(self, figura: dict):
        if figura.get("tipo") == "circulo":
            return math.pi * figura["radio"]**2
        
        # Rectángulo: {'tipo': 'rectangulo', 'base': valor, 'altura': valor}
        if figura.get("tipo") == "rectangulo":
            return figura["base"] * figura["altura"]

        # Triángulo: {'tipo': 'triangulo', 'base': valor, 'altura': valor}
        if figura.get("tipo") == "triangulo":
            return (figura["base"] * figura["altura"]) / 2

        # Trapecio: {'tipo': 'trapecio', 'base_mayor': valor, 'base_menor': valor, 'altura': valor}
        if figura.get("tipo") == "trapecio":
            return ((figura["base_mayor"] + figura["base_menor"]) * figura["altura"]) / 2

        # Pentágono regular: {'tipo': 'pentagono', 'lado': valor}
        if figura.get("tipo") == "pentagono":
            lado = figura["lado"]
            apotema = lado / (2 * math.tan(math.pi / 5))
            perimetro = 5 * lado
            return (perimetro * apotema) / 2

        raise ValueError("Tipo de figura desconocido")


figura = FiguraGeometrica()

print("Área del círculo:", figura.area({"tipo": "circulo", "radio": 5}))
print("Área del rectángulo:", figura.area({"tipo": "rectangulo", "base": 4, "altura": 6}))
print("Área del triángulo:", figura.area({"tipo": "triangulo", "base": 4, "altura": 6}))
print("Área del trapecio:", figura.area({"tipo": "trapecio", "base_mayor": 6, "base_menor": 4, "altura": 5}))
print("Área del pentágono:", figura.area({"tipo": "pentagono", "lado": 3}))
