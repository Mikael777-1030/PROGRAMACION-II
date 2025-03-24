import math

class Estadistica:
    def __init__(self, numeros):
        if len(numeros) != 10:
            raise ValueError("Debe ingresar exactamente 10 números.")
        self.numeros = numeros

    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def desviacion(self):
        promedio = self.promedio()
        return math.sqrt(sum((x - promedio) ** 2 for x in self.numeros) / (len(self.numeros) - 1))

    def mostrar_resultados(self):
        " Muestra los resultados de las estadísticas "
        print(f"El promedio es {self.promedio():.2f}")
        print(f"La desviación estándar es {self.desviacion():.5f}")

def obtener_numeros():
    " Solicita 10 números al usuario "
    while True:
        try:
            numeros = list(map(float, input("Ingrese 10 números: ").split()))
            return numeros
        except ValueError:
            print("Error: Ingrese solo números.")


try:
    numeros = obtener_numeros()
    estadistica = Estadistica(numeros)
    estadistica.mostrar_resultados()
except ValueError as e:
    print(e)
