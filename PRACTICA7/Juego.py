import random

class Juego:
    def __init__(self, numero_de_vidas):
        self.numero_de_vidas = numero_de_vidas
        self.record = 0

    def reinicia_partida(self):
        self.numero_de_vidas = 3

    def actualiza_record(self):
        self.record += 1

    def quita_vida(self):
        self.numero_de_vidas -= 1

    def valida_numero(self, numero):
        return 0 <= numero <= 10

class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas, numero_adivinar):
        super().__init__(vidas)
        self.numero_adivinar = numero_adivinar

    def juego(self):
        while self.numero_de_vidas > 0:
            intento = int(input("Adivina el número (0 al 10): "))
            if self.valida_numero(intento):
                if intento == self.numero_adivinar:
                    print("¡Acertaste!")
                    self.actualiza_record()
                    break
                else:
                    print("Fallaste.")
                    self.quita_vida()
            else:
                print("Número fuera de rango.")

        if self.numero_de_vidas == 0:
            print("Te quedaste sin vidas.")

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 == 0:
            return True
        print("Número no válido: debe ser PAR entre 0 y 10.")
        return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def valida_numero(self, numero):
        if 0 <= numero <= 10 and numero % 2 != 0:
            return True
        print("Número no válido: debe ser IMPAR entre 0 y 10.")
        return False


if __name__ == "__main__":
    juego1 = JuegoAdivinaNumero(3, 5)
    juego2 = JuegoAdivinaPar(3, 4)
    juego3 = JuegoAdivinaImpar(3, 7)

    juego1.juego()
    juego2.juego()
    juego3.juego()
