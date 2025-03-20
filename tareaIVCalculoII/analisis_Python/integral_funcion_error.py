import math
import numpy as np

class Datos():
    def __init__(self):
        pass
    def ingresar_n(self):
        while True:
            try:
                self.n = int(input("Inserte el valor de n: "))
                break
            except Exception as e:
                print(e)
    def ingresar_a(self):
        while True:
            try:
                self.a = input("Inserte el valor de a: ")
                break
            except Exception as e:
                print(e)
    def ingresar_b(self):
        while True:
            try:
                self.b = input("Inserte el valor de b: ")
                break
            except Exception as e:
                print(e)
    
 

class Metodos:
    def __init__(self, n: int, a: str, b: str):
        self.n = n
        self.a = self.convertir_valor(a)
        self.b = self.convertir_valor(b)
        self.k = (self.b - self.a) / self.n

    def convertir_valor(self, valor):
        valor = valor.replace('pi', 'math.pi')
        valor = valor.replace('e', 'math.e')
        return float(eval(valor))
            

class Trapecio(Metodos):
    def __init__(self, n: int, a: str, b: str):
        super().__init__(n, a, b)

    def sumatoria(self, funcion: Metodos):
        x = np.zeros(self.n + 1)

        for i in range(0, self.n + 1):
            x[i] = self.a + self.k * i

        suma = 0
        for i in range(1, self.n):
            suma += funcion(- x[i] ** 2)

        return self.k * (((1/2) * funcion(- x[0] ** 2)) + (suma) + ((1/2) * funcion(- x[self.n] ** 2)))



condiciones = Datos()

condiciones.ingresar_n()
condiciones.ingresar_a()
condiciones.ingresar_b()


fx = math.exp

aproxTrapecio = Trapecio(condiciones.n, condiciones.a, condiciones.b)
print("\nMétodo del Trapecio: ")
print(f"Aproximación: {aproxTrapecio.sumatoria(fx)}")
