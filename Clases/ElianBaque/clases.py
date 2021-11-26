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

# Ejercicio 3
# Suma y Resta es Entre columnas verticales. En la resta se cambia el signo a la segunda matriz y se hace la operacion.
class Matris3D: # Se que no se ponen numeros para crear, pero era para no perderme tanto

    def __init__(self, matris , matrisDos):
        self.matris = matris
        self.matrisDos = matrisDos

    def Suma(self):
        
        newcolumnX = []
        newcolumnY = []
        newcolumnZ = []
        count = 0
        countDos = 0
        countTres = 0

        for x in self.matris["columnaX"]:
            newcolumnX.insert(count, x + self.matrisDos["columnaX"][count]) 
            count += 1
        for x in self.matris["columnaY"]:
            newcolumnY.insert(countDos, x + self.matrisDos["columnaY"][countDos]) 
            countDos += 1        
        for x in self.matris["columnaZ"]:
            newcolumnZ.insert(countTres, x + self.matrisDos["columnaZ"][countTres]) 
            countTres += 1

        MatrisFinal = {
            "columnX" : newcolumnX,
            "columnY" : newcolumnY,
            "columnZ" : newcolumnZ
        }

        return print(MatrisFinal)
        



# Va queriendo eso , tengo que pensarlo un poco mas
MiMatris = Matris3D({
            "columnaX" : [1,4,5],
            "columnaY" : [7,2,5],
            "columnaZ" : [1,4,5]
        },{                             # Ingresar matrises a Sumar, restar y multiplicar
            "columnaX" : [9,7,41],
            "columnaY" : [7,2,5],
            "columnaZ" : [1,4,5]
        }) 

MiMatris.Suma()


