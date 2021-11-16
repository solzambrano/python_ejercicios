# Ejercicio 1

cadena="soy una cadena"

def replaceString(cadena):
   cadena= cadena.replace(" ","-")
   return cadena

replaceString(cadena)

# Ejercicio 2

string = "Cambiando to upper case o LOWER CASE"

def changeFont(string):
    """Intercambia el las minisculas a mayusculas y viceversa"""
    swap = string.swapcase()
    return swap

print(changeFont(string))

# Ejercicio 3
oracion = "Las vacas locas son rojas"
letra = "Z"
num = 8
def inmutable(texto, posicion, letra):
    """Cambia un letra en X posicion del String"""

    ListString = list(texto)
    ListString[posicion] = letra
    ListString = "".join(ListString)

    return  print(ListString)

inmutable(oracion, num, letra)

# Ejercicio 4

nomYape="nombre apellido"

def replaceNameAndSurname(cadena):
    return cadena.title()
    
# Ejercicio 5

resultados = [2,4,6,2,3,7,9,8,5]

def segundoPuesto(lista):
    puestos = []
    
    for resultado in lista:
        
        if resultado not in puestos:
            puestos.append(resultado)
            
    puestos.sort()
    return puestos[(len(puestos)-2)]

print(segundoPuesto(resultados))

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

