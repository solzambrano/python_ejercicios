string = "Cambiando to upper case o LOWER CASE"

def changeFont(string):
    """Intercambia el las minisculas a mayusculas y viceversa"""
    swap = string.swapcase()
    return swap

print(changeFont(string))

""" Extra: a- Escribir una funcion que recibe un numero entero
y imprima por salida estandar(usando print) un triangulo de numeros 
de altura igual al numero ingresado. Ej. Si se ingresa el numero 5, debe imprimir: 1 22 333 4444 55555 """