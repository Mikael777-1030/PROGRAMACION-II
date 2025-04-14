
class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def incrementaYZ(self):
        self.y += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)

    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1

if __name__ == "__main__":
    d = D(1, 2, 3)
    
    print("Valores iniciales:")
    print("x =", d.x)
    print("y =", d.y)
    print("z =", d.z)

    d.incrementaXYZ()
    print("\nDespués de incrementaXYZ():")
    print("x =", d.x)
    print("y =", d.y)
    print("z =", d.z)

    d.incrementaXZ()
    print("\nDespués de incrementaXZ():")
    print("x =", d.x)
    print("z =", d.z)

    d.incrementaYZ()
    print("\nDespués de incrementaYZ():")
    print("y =", d.y)
    print("z =", d.z)

    d.incrementaZ()
    print("\nDespués de incrementaZ():")
    print("z =", d.z)
