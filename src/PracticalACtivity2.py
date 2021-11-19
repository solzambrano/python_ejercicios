# Actividad Practica - Python Unidad 2

# 1) Desarrollar una función que reciba tres números positivos y devuelva el mayor 
    # de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor 
    # estricto devolver -1. No utilizar operadores lógicos (and, or, not).
    # Desarrollar también un programa para ingresar los tres valores, invocar a la función y 
    # mostrar el máximo hallado, o un mensaje informativo si éste no existe

numbers = []

for i in range(3):
    numbers.append(int(input("Ingrese un numero: ")))

def duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return -1
    return False
            
if duplicates(numbers) == -1:
    print("No hay un numero mayor estricto")
else:
    print("El numero mayor estricto es: ", max(numbers))

# 2) Desarrollar una función que reciba tres números enteros positivos y verifique si 
    # corresponden a una fecha válida (día, mes, año). Devolver True o False según 
    # la fecha sea correcta o no. Realizar también un programa para verificar el 
    # comportamiento de la función

def positiveInteger(number):
    if number < 0:
        return False
    else:
        return True

numbers = []

for i in range(3):
    number = int(input("Ingrese un numero: "))
    if(positiveInteger(number)):
        numbers.append(number)

def validDate(numbers):
    if len(numbers) != 3:
        return False
    elif numbers[0] > 31 or numbers[0] < 1:
        return False
    elif numbers[1] > 12 or numbers[1] < 1:
        return False
    elif numbers[2] > 2100 or numbers[2] < 1900:
        return False
    else:
        return True