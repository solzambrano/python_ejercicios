# Ejercicio 2

string = "Cambiando to upper case o LOWER CASE"

def changeFont(string):
    """Intercambia el las minisculas a mayusculas y viceversa"""
    swap = string.swapcase()
    return swap

print(changeFont(string))

# Ejercicio 1

cadena="soy una cadena"

def replaceString(cadena):
   cadena= cadena.replace(" ","-")
   return cadena

replaceString(cadena)

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