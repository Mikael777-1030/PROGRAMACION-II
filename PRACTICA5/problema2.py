import math

def calcular_promedio(numeros):
    " Calcula el promedio de una lista de números "
    return sum(numeros) / len(numeros)

def calcular_desviacion(numeros, promedio):
    " Calcula la desviación estándar de una lista de números "
    return math.sqrt(sum((x - promedio) ** 2 for x in numeros) / (len(numeros) - 1))

def estadisticas():
    " Solicita 10 números y muestra el promedio y la desviación estándar "
    try:
        numeros = list(map(float, input("Ingrese 10 números: ").split()))
        if len(numeros) != 10:
            print("Error: Debe ingresar exactamente 10 números.")
            return
        
        promedio = calcular_promedio(numeros)
        desviacion = calcular_desviacion(numeros, promedio)

        print(f"El promedio es {promedio:.2f}")
        print(f"La desviación estándar es {desviacion:.5f}")
    except ValueError:
        print("Error: Ingrese solo números.")

# Ejecutar la función
estadisticas()
