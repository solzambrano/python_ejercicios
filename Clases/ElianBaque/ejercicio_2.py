# Ejercicio 2

class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y 
        self.z = z

    def Suma(self, EjeX, EjeY, EjeZ):
        resultadoX = self.x + EjeX
        resultadoY = self.y + EjeY
        resultadoZ = self.z + EjeZ
        vector = (resultadoX, resultadoY, resultadoZ)
        return vector

    def Resta(self, EjeX, EjeY, EjeZ):
        resultadoX = self.x - EjeX
        resultadoY = self.y - EjeY
        resultadoZ = self.z - EjeZ
        vector = (resultadoX, resultadoY, resultadoZ)
        return vector
    
    def Multi(self, EjeX, EjeY, EjeZ):
        resultadoX = self.x * EjeX
        resultadoY = self.y * EjeY
        resultadoZ = self.z * EjeZ
        vector = (resultadoX, resultadoY, resultadoZ)
        return vector

    def Divicion(self, EjeX, EjeY, EjeZ): # La divicion no se si esta bien. No encontre algo que explique la divicion
        resultadoX = float(self.x / EjeX)   # entre vectores tridimencionales
        resultadoY = float(self.y / EjeY)
        resultadoZ = float(self.z / EjeZ)
        vector = (resultadoX, resultadoY, resultadoZ)
        return vector

        