import numpy as np

class AlgebraVectorial:
    
    @staticmethod
    def son_perpendiculares_a_b(a, b):
        return np.linalg.norm(a + b) == np.linalg.norm(a - b)
    
    @staticmethod
    def son_mutuamente_perpendiculares(a, b):
        return np.linalg.norm(a + b) == np.linalg.norm(a - b) and np.linalg.norm(a) == np.linalg.norm(b)

    @staticmethod
    def producto_punto(a, b):
        return np.dot(a, b) == 0

    @staticmethod
    def norma_cuadrado(a):
        return np.linalg.norm(a) ** 2

    @staticmethod
    def son_paralelos_escalar(a, b):
        if np.all(b == 0):
            return False
        r = a / b
        return np.all(r == r[0])

    @staticmethod
    def son_paralelos_producto_cruz(a, b):
        return np.cross(a, b) == 0

    @staticmethod
    def proyeccion_ortogonal(a, b):
        return (np.dot(a, b) / np.dot(b, b)) * b if np.dot(b, b) != 0 else None

    @staticmethod
    def componente_en_b(a, b):
        return np.dot(a, b) / np.linalg.norm(b) if np.linalg.norm(b) != 0 else None



a = np.array([3, 4])
b = np.array([6, 8])

print("¿Son perpendiculares?", AlgebraVectorial.son_perpendiculares_a_b(a, b))
print("Proyección de a sobre b:", AlgebraVectorial.proyeccion_ortogonal(a, b))
print("Componente de a en dirección de b:", AlgebraVectorial.componente_en_b(a, b))
