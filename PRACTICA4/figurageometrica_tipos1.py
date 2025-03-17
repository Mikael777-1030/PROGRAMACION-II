'''
Calcular el área de diferentes figuras
geométricas usando el mismo nombre de método.
'''
import math
class FiguraGeometrica:
    def area(self, a, b=None, c=None, d=None, e=None):
        if isinstance(a, float) and b is None and c is None and d is None and e is None:
            return math.pi * a * a
        elif isinstance(a, float) and isinstance(b, float) and c is None and d is None and e is None:
            return a * b 
        elif isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and d is None and e is None:
            return (a * b) / 2 
        elif isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and isinstance(d, float) and e is None:
            return (a + b) * c / 2 
        elif isinstance(a, float) and isinstance(b, float) and isinstance(c, float) and isinstance(d, float) and isinstance(e, float):
            return 5 * a * a / (4 * math.sqrt(5 - 2 * math.sqrt(5))) 

figura = FiguraGeometrica()
print("Área del círculo:", figura.area(5.0))
print("Área del rectángulo:", figura.area(4.0, 6.0))
print("Área del triángulo:", figura.area(4.0, 6.0, 0.0))
print("Área del trapecio:", figura.area(6.0, 4.0, 5.0, 0.0))
print("Área del pentágono:", figura.area(3.0, 0.0, 0.0, 0.0, 0.0))



