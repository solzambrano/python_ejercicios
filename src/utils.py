# Ejercicio 2

string = "Cambiando to upper case o LOWER CASE"

def changeFont(string):
    """Intercambia el las minisculas a mayusculas y viceversa"""
    swap = string.swapcase()
    return swap

print(changeFont(string))

""" Extra: a- Escribir una funcion que recibe un numero entero
y imprima por salida estandar(usando print) un triangulo de numeros 
de altura igual al numero ingresado. Ej. Si se ingresa el numero 5, debe imprimir: 1 22 333 4444 55555 """

# Ejercicio 1

cadena="soy una cadena"

def replaceString(cadena):
   cadena= cadena.replace(" ","-")
   return cadena

replaceString(cadena)

# ejercicio4
nomYape="nombre apellido"

def replaceNameAndSurname(cadena):
    return cadena.title()
    

print(replaceNameAndSurname(nomYape))
# Ejercicio Extra 

def triangulo(num):
    punta = 1
    while punta != num + 1:
        string = ""
        for i in range(punta):
            string += str(punta) 
        print(string)
        string = ""
        punta += 1

triangulo(7)
