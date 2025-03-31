import numpy as np

class AlgebraVectorial3D:
    
    def __init__(self, x, y, z):
        self.vector = np.array([x, y, z])
    
    def __add__(self, other):
        return AlgebraVectorial3D(*(self.vector + other.vector))

    def __mul__(self, escalar):
        return AlgebraVectorial3D(*(self.vector * escalar))

    def norma(self):
        return np.linalg.norm(self.vector)

    def normalizar(self):
        norma = self.norma()
        return AlgebraVectorial3D(*(self.vector / norma)) if norma != 0 else None

    def producto_punto(self, other):
        return np.dot(self.vector, other.vector)

    def producto_cruz(self, other):
        return AlgebraVectorial3D(*np.cross(self.vector, other.vector))

    def __str__(self):
        return f"({self.vector[0]}, {self.vector[1]}, {self.vector[2]})"



a = AlgebraVectorial3D(1, 2, 3)
b = AlgebraVectorial3D(4, 5, 6)

print("Suma:", a + b)
print("Multiplicación por escalar:", a * 3)
print("Norma de a:", a.norma())
print("Vector normalizado de a:", a.normalizar())
print("Producto punto de a y b:", a.producto_punto(b))
print("Producto cruz de a y b:", a.producto_cruz(b))
