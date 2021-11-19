# Actividad Practica - Python Unidad 1

# 1) Escribe un programa que escrbia en la pantalla "Hello World".

print("Hello World")

# 2) Escribe un programa que escrbia en la pantalla el resultado de sumar 3 + 5.

print(3 + 5)

# 3) Escribe un programa que pida el nombre del usuario y escrbia un tesal "Hola, nombre_usuario".

name_User = input("Introduce tu nombre: ")
print("Hola, " + name_User)


# 4) Escribe un programa que pida un numero, pida otro numero y escrbia el resultado de sumar estos dos numeros.

value_1 = int(input("Introduce un numero: "))
value_2 = int(input("Introduce otro numero: "))
sum = value_1 + value_2
print(f'La suma de {value_1} + {value_2} = {sum}')

# 5) Escribe un programa que pida dos numeros y escriba en la pantalla el mayor de los tres

values = []

values.append(int(input("Introduce un numero: ")))
values.append(int(input("Introduce un numero: ")))


def calculateMaximum(values):
    max = 0
    flag = 0
    for i in range(0, len(values)):
        if flag == 0 or values[i] > max:
            max = values[i]
            flag = 1
    return max


print(f"El numero mas grande es:  {calculateMaximum(values)} ")


# 6) Escribe un programa que pida 3 numero y escriba en la pantalla el mayor de los tres.

values = []
values.append(int(input("Introduce un numero: ")))
values.append(int(input("Introduce un numero: ")))
values.append(int(input("Introduce un numero: ")))

print(f"El numero mas grande de los 3 es:  {calculateMaximum(values)} ")

# 7) Escribe un programa que pida un número y diga si es divisible por 2.


def divisibleby2():
    number = int(input("Introduce un numero: "))
    if number % 2 == 0:
        print("El numero es divisible por 2")
    else:
        print("El numero no es divisible por 2")


divisibleby2()

# 8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro).

number = int(input("Introduce un numero: "))


def isDivisible(number):
    str = 'es divisible por '
    if number % 2 == 0:
        str += '2, '
    if number % 3 == 0:
        str += '3, '
    if number % 5 == 0:
        str += '5, '
    if number % 7 == 0:
        str += '7'

    print(str)

# 9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)

isDivisible(number)

# hecho en el punto 8

# 10)  Escribir un programa que escriba en pantalla los divisores de un número dado

number = int(input("Introduce un numero: "))
contador = 0
for divisor in range(1,number+1):
    if (number % divisor) == 0 :
        print(divisor,"es divisor")
        contador += 1
print("el numero ",number," tiene ",contador," divisores")

# 11) Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)

def isprime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True

if isprime(int(input("Introduce un numero: "))):
    print("El numero es primo")
else:
    print("El numero no es primo")

# 12) Pide una nota (número). Muestra la calificación según la nota:  0-3: Muy deficiente, 3-5: Insuficiente, 5-6: Suficiente, 6-7: Bien, 7-9: Notable, 9-10: Sobresaliente.                                         

def qualification(nota):
    if nota <= 3:
        print("Muy deficiente")
    elif nota <= 5:
        print("Insuficiente")
    elif nota <= 6:
        print("Suficiente")
    elif nota <= 7:
        print("Bien")
    elif nota <= 9:
        print("Notable")
    else:
        print("Sobresaliente")

qualification(int(input("Introduce una nota: ")))


# 13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma
"""         1
            22
            333
            4444
            55555
            666666"""


def pyramid(number):
    for i in range(1, number+1):
        print(str(i) * i)


pyramid(int(input("Introduce un numero: ")))