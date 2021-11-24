# Ejercicio 1 Pensado con complejo positivo
class MathComplex:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Suma(self, real, imaginario):
        resultado = str(self.a + real) + " + " + str(self.b + imaginario) + "i"
        return resultado

    def Resta(self, real, imaginario):
        if(self.b - imaginario > 0):
            ResImaginario = " + " + str(self.b - imaginario) + "i"
        else:
            ResImaginario = str(self.b - imaginario) + "i"
        resultado = str(self.a - real) + ResImaginario
        return resultado

    def Multi(self, real, imaginario):
        resultado = str(self.a * real) + " + " + str(self.b * imaginario) + "i"
        return resultado

    def Div(self, real, imaginario):
        resultado = resultado = str(self.a / real) + " + " + str(self.b / imaginario) + "i"
        return resultado

Objeto = MathComplex(6, 7)
print(Objeto.Suma(9, 8))
print(Objeto.Resta(7, 2))
print(Objeto.Multi(6, 2))
print(Objeto.Div(3, 7)) # Condicion si es flotante o no Para despues