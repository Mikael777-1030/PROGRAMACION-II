import math

class FiguraGeometrica:
    
    def area(self, *args):
        """ Calcula el área según la cantidad de argumentos. """
        if len(args) == 1:  
            # Círculo (radio)
            radio = args[0]
            return math.pi * radio**2
        
        elif len(args) == 2:  
            # Rectángulo (base, altura)
            base, altura = args
            return base * altura

        elif len(args) == 3:  
            # Triángulo (base, altura, ignorado)
            base, altura, _ = args
            return (base * altura) / 2
        
        elif len(args) == 4:  
            # Trapecio (base mayor, base menor, altura, ignorado)
            base_mayor, base_menor, altura, _ = args
            return ((base_mayor + base_menor) * altura) / 2
        
        elif len(args) == 5:  
            # Pentágono regular (solo lado)
            lado = args[0]
            apotema = lado / (2 * math.tan(math.pi / 5))
            perimetro = 5 * lado
            return (perimetro * apotema) / 2
        
        else:
            raise ValueError("Número de argumentos no válido para una figura conocida")

figura = FiguraGeometrica()

print("Área del círculo:", figura.area(5))
print("Área del rectángulo:", figura.area(4, 6))
print("Área del triángulo:", figura.area(4, 6, 0))
print("Área del trapecio:", figura.area(6, 4, 5, 0))
print("Área del pentágono:", figura.area(3, 0, 0, 0, 0))
