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

def ejercicio2():
    numbers = []
    for i in range(3):
        number = int(input("Ingrese un numero: "))
        if(positiveInteger(number)):
            numbers.append(number)
    if (len(numbers) == 3):
        validDate(numbers)
    else :
        print("No se ingresaron 3 numeros")


# 3) Un comercio de electrodomésticos necesita para su línea de cajas un programa 
   # que le indique al cajero el cambio que debe entregarle al cliente. Para eso se 
   # ingresan dos números enteros, correspondientes al total de la compra y al 
   # dinero recibido. Informar cuántos billetes de cada denominación deben ser 
   # entregados al cliente como vuelto, de tal forma que se minimice la cantidad de 
   # billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. 
   # Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la 
   # compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de 
   # $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.

def returnChange(total, money):
    if money < total:
        print("No se puede devolver el dinero")
    else:
        change = money - total
        print("El cambio debe ser: ")
        if change >= 500:
            print(change // 500, "billetes de 500") # operator // devuelve el numero sin coma
            change = change % 500
        if change >= 100:
            print(change // 100, "billetes de 100")
            change = change % 100
        if change >= 50:
            print(change // 50, "billetes de 50")
            change = change % 50
        if change >= 20:
            print(change // 20, "billetes de 20")
            change = change % 20
        if change >= 10:
            print(change // 10, "billetes de 10")
            change = change % 10
        if change >= 5:
            print(change // 5, "billetes de 5")
            change = change % 5
        if change >= 1:
            print(change // 1, "billetes de 1")
            change = change % 1

returnChange(int(input("Ingrese el total de la compra: ")), int(input("Ingrese el dinero recibido: ")))


# 4) Escribir dos funciones separadas para imprimir por pantalla los siguientes 
   # patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:


def asteriscos(n):
    for i in range(n):
        if i !=0 :
            print("*" * (i*2))

asteriscos(5)

def asteriscosCuadrado(n):
    for i in range(n):
        print("*" * (n*2))

asteriscosCuadrado(5)

# 5) Crear una función lambda que devuelva el cuadrado de un valor recibido cómo 
   # parámetro. Desarrollar además un programa para verificar el comportamiento 
   # de la función.

b = lambda x: x*2

print(b(int(input("Ingrese un numero: "))))

# 6) Crear una función lambda para comprobar si un número es par o impar.
   # Desarrollar además un programa para verificar el comportamiento de la 
   # función.

even = lambda x: x % 2 == 0 
odd = lambda x: x % 2 != 0

def ejercicio6():
    number = int(input("Ingrese un numero: "))
    if even(number):
        print("El numero es par")
    elif odd(number):
        print("El numero es impar")

ejercicio6()


# 7) Crear una lista con los cuadrados de los números entre 1 y N (ambos 
   # incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los 
   # últimos 10 valores de la lista.

def cuadrados(n):
    numbers = []
    for i in range(1, n):
        numbers.append(i)
        numbers.append(i**2)
    print(numbers[-10:])

cuadrados(int(input("Ingrese un numero: ")))


# 8) Eliminar de una lista de palabras que se encuentren en una segunda lista. 
   # Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

list1= ["hola", "mundo", "como", "estas"]
list2= ["hola", "mundo", "estas"]
listremove = []
listresult = []
for i in list1:
    flag=True
    for j in list2:
        if i == j:
            listremove.append(i)
            flag=False
    if flag:
        listresult.append(i)
    

print("Lista original: ", list1)
print("Lista a eliminar: ", list2)
print("Lista resultante: ", listresult)

# 9) Escribir una función que reciba una lista como parámetro y devuelva True si la 
   # lista está ordenada en forma ascendente o False en caso contrario. Por 
   # ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. 
   # Desarrollar además un programa para verificar el comportamiento de la 
   # función.

listOrder = [1, 2, 3]
listDesorder = ['b', 'a']

def isOrder(list):
    if list == sorted(list):
        return True
    else:
        return False


print(isOrder(listOrder))
print(isOrder(listDesorder))

# 10) Desarrollar una función que determine si una cadena de caracteres es capicúa, 
    # sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que 
    # permita verificar su funcionamiento.
    # https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html
    # x[:5]  # first five elements
    # x[5:]  # elements after index 5
    # x[4:7]  # middle sub-array
    # x[::2]  # every other element
    # x[1::2]  # every other element, starting at index 1
    # x[::-1]  # all elements, reversed
    # x[5::-2]  # reversed every other from index 5
def isCapicúa (string):
    if string == string[::-1]:
        return True
    else:
        return False

# 11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que 
    # la misma tiene 80 columnas.

    #NO ENTIENDO BIEN ESTO

# Me canse de hacerlo, pero me gustaria que me ayudaran a ver como funciona el 11 en adelante.
