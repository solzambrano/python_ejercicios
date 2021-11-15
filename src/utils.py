string = "Cambiando to upper case o LOWER CASE"

def changeFont(string):
    """Intercambia el las minisculas a mayusculas y viceversa"""
    swap = string.swapcase()
    return swap


print(changeFont(string))

cadena="soy una cadena"

def replaceString(cadena):
   cadena= cadena.replace(" ","-")
   return cadena

replaceString(cadena)

resultados = [2,4,6,2,3,7,9,6,5]

def segundoPuesto(lista):
    puestos = []
    
    for resultado in lista:
        
        if resultado not in puestos:
            puestos.append(resultado)
            

    return ((len(puestos)-1))

print(segundoPuesto(resultados))