class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0  

    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio:.2f}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        if dias_anticipacion > 10:
            self.precio = 80.0
        else:
            self.precio = 100.0

class Galeria(Boleto):
    def __init__(self, numero, edad):
        super().__init__(numero)
        if edad < 15 or edad > 60:
            self.precio = 25.0
        else:
            self.precio = 50.0

def main():
    while True:
        print("\n--- Teatro Municipal ---")
        print("1. Comprar boleto")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '2':
            print("Gracias por usar el sistema.")
            break

        numero = input("Ingrese el número del boleto: ")
        print("Tipo de boleto:\n1. Palco\n2. Platea\n3. Galería")
        tipo = input("Seleccione el tipo (1/2/3): ")

        if tipo == '1':
            boleto = Palco(numero)
        elif tipo == '2':
            dias = int(input("Ingrese días de anticipación: "))
            boleto = Platea(numero, dias)
        elif tipo == '3':
            edad = int(input("Ingrese la edad del comprador: "))
            boleto = Galeria(numero, edad)
        else:
            print("Opción no válida.")
            continue

        print("Boleto generado:")
        print(boleto)

if __name__ == "__main__":
    main()
