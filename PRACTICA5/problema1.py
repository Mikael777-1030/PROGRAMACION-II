import math

def get_discriminante(a, b, c):
    """ Calcula el discriminante de la ecuación cuadrática """
    return b**2 - 4*a*c

def get_raiz1(a, b, discriminante):
    """ Calcula la primera raíz si el discriminante es positivo """
    return (-b + math.sqrt(discriminante)) / (2 * a)

def get_raiz2(a, b, discriminante):
    """ Calcula la segunda raíz si el discriminante es positivo """
    return (-b - math.sqrt(discriminante)) / (2 * a)

def resolver_ecuacion_cuadratica():
    """ Solicita al usuario los coeficientes y muestra la solución de la ecuación """
    try:
        a, b, c = map(float, input("Ingrese a, b, c: ").split())
        if a == 0:
            print("No es una ecuación cuadrática válida (a ≠ 0).")
            return

        discriminante = get_discriminante(a, b, c)

        if discriminante > 0:
            r1 = get_raiz1(a, b, discriminante)
            r2 = get_raiz2(a, b, discriminante)
            print(f"La ecuación tiene dos raíces {r1:.5f} y {r2:.5f}")
        elif discriminante == 0:
            r1 = -b / (2 * a)
            print(f"La ecuación tiene una raíz {r1:.5f}")
        else:
            print("La ecuación no tiene raíces reales")
    except ValueError:
        print("Error: Debe ingresar tres números separados por espacios.")

# Ejecutar la función
resolver_ecuacion_cuadratica()
