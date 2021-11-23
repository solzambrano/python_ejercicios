# Ejercicio 1

#cadena="soy una cadena"

def replaceString(cadena):
   cadena= cadena.replace(" ","-")
   return cadena

#replaceString(cadena)

# Ejercicio 2

#string = "Cambiando to upper case o LOWER CASE"

def changeFont(string):
    """Intercambia el las minisculas a mayusculas y viceversa"""
    swap = string.swapcase()
    return swap

#print(changeFont(string))

# Ejercicio 3
#oracion = "Las vacas locas son rojas"
#letra = "Z"
#num = 8
def inmutable(texto, posicion, letra):
    """Cambia un letra en X posicion del String"""

    ListString = list(texto)
    ListString[int(posicion)] = letra
    ListString = "".join(ListString)

    return  ListString

#inmutable(oracion, num, letra)

# Ejercicio 4

#nomYape="nombre apellido"

def replaceNameAndSurname(cadena):
    return cadena.title()
    
# Ejercicio 5

#resultados = [2,4,6,2,3,7,9,8,5]

def segundoPuesto(lista_str):
    lista=map(int, lista_str.split(","))

    puestos = []
    
    for resultado in lista:
        
        if resultado not in puestos:
            puestos.append(resultado)
            
    puestos.sort()
    print(puestos)
    return puestos[(len(puestos)-2)]

#print(segundoPuesto(resultados))

#print(replaceNameAndSurname(nomYape))

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

#triangulo(7)

def countMostUsedCharaters(string):
    letras_dic = dict()  #Guarda repetición de letras
    string = string.replace(" ","") #Elimina espacios
    string = string.lower() # Convierte a minusculas
    for letra in string: #Por cada letra
        if letra in letras_dic: #Si ya estaba en el dic() significa que se repite
            letras_dic[letra] += 1 #Continua el conteo
        else:
            letras_dic[letra] = 1 #Si la letra no esta en el diccionario, la agrega
    # print(letras_dic) #{'c': 2, 'o': 4, 'd': 2, 'a': 1}
    letras_dic = dict(sorted(letras_dic.items(), key=lambda item: item[1])) #Ordena el diccionario por valor
    #print(letras_dic) #{'a': 1, 'c': 2, 'd': 2, 'o': 4}
    masUsados = list(letras_dic.items())[-3:] #Obtiene los ultimos 3 del diccionario
    print(masUsados)
    

#countMaxCharaters("Codo a Codo") #[('c', 2), ('d', 2), ('o', 4)]