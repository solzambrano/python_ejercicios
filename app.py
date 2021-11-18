from src.utils import *


isRuning = True

while isRuning:
    print("Ingrese el comando deseado o help para ayuda")
    comando = input()

    if comando == "help":
        print ("#0 Salir()                             --> Salir del programa")
        print ("#1 replaceString(cadena)               --> Cambia espacios de un String por -")
        print ("#2 changeFont(string)                  --> Intercambia el las minisculas a mayusculas y viceversa")
        print ("#3 inmutable(texto, posicion, letra)   --> Cambia un letra en X posicion del String")
        print ("#4 replaceNameAndSurname(cadena)       --> Capitalize Nombre y Apellido")
        print ("#5 segundoPuesto(lista)                --> Devuelve la puntuacion del subcampeón")
        print ("E1 triangulo(num)                      --> Triangulo de numeros de altura igual al numero ingresado")

    elif comando == "1":
        cadena=input("Ingrese el texto que desea modificar: ")
        print (replaceString(cadena))
    
    elif comando =="2":
        string = input("Ingrese el texto que desea modificar: ")
        print (changeFont(string))
    
    elif comando =="3":
        texto = input("Ingrese el texto original: ")
        posicion=input("Ingrese la posición del cursor: ")
        letra=input("Ingrese el caracter a de reemplazo: ")
        print(inmutable(texto, posicion, letra))
    
    elif comando =="4":
        cadena=input("Ingrese el nombre y apellido: ")
        print(replaceNameAndSurname(cadena))
    
    elif comando=="5":
        lista=input("ingrese la lista de puntajes separados por comas: ")
        print("El segundo puesto tiene un puntaje de ", segundoPuesto(lista))
    
    elif comando=="E1":
        num=int(input("Ingrese la altura del triángulo: "))
        triangulo(num)
    
    elif comando =="0":
        exit()
    
    else:
        print("Comando no válido")

    