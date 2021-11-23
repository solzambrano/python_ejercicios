"""
1-Crear una clase que represente un numero complejo. Tenga 4 metodos que permita las operaciones matematicas basicas (+,-,*,/).

2-Crear una clase que represente un vector de 3 dimensiones.
Tenga 4 metodos que permitan las operaciones matematicas basicas (+,-,* y / por un escalar).

3-Crear una clase que represente una matriz de 3x3 dimensiones. Tengan 3 metodos que permitan
las operaciones matematicas basicas (excluimos la division) (+ y - entre matrices, * solo por un vector).

4-Crear una clase que represente al perfil usuario que ademas tenga una relacion (herencia) con estas dos clases: 
administrador y reportero (solo tiene lectura de datos). El usuario tiene objeto carrito de compras.
El administrador puede ver a todos los usuarios y lo que tenga adentro. El reporter solo ve todos los carritos de compra.

5-Escribir una nueva class que herede de server.py y que maneje la conexion con el cliente y repita el mensaje enviado por el cliente.

6-Escribir una nueva class que herede de server.py y que maneje solo informacion en JSON."""

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

# Ejercicio 2