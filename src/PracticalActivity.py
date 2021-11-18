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
        str + '2, '
    if number % 3 == 0:
        str + '3, '
        if number % 5 == 0:
            str + '5, '
        if number % 7 == 0:
            str + '7'

    print(str)
