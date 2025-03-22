""" 1. Calculadora básica con funciones
Crea una función llamada calculadora que recibe dos números y una operación (+, -, *, /) como parámetros. Devuelve el resultado de la operación. 
Si la operación no es válida, devuelve un mensaje de error."""

def calculadora(a, b, operacion):
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        if b != 0:
            return a / b
        else:
            return("No se puede dividir entre cero.")
    else:
        return("Parámetro inválido.")

resultado = calculadora(10, 2, "/")
print(resultado)

"""🔢 2. Número par o impar
Escribe una función llamada es_par que reciba un número y devuelva True si es par y False si es impar. 
Luego, crea un programa que pida al usuario un número y use la función para decir si es par o impar."""

def es_par(num):
    return num % 2 == 0
    
num = int(input("Introduce un número: "))

result = es_par(num)
print("¿El número es par?", result)

""" 3. Área de figuras geométricas
Crea una función calcular_area que reciba el nombre de una figura geométrica (círculo, cuadrado, triángulo) 
y sus dimensiones necesarias (radio, lado o base y altura). 
Devuelve el área de la figura. Si la figura no es válida, muestra un mensaje de error."""

pi = 3.1416

def calcular_area(figura, radio=None, lado=None, base=None, altura=None):
    if figura == "círculo" or figura == "circulo":
        return pi * radio**2
    elif figura == "cuadrado":
        return lado * lado
    elif figura == "triángulo" or figura == "triangulo":
        return (base * altura) / 2
    else:
        return "Error, datos no válidos."
    
figura = input("Introduce la figura (círculo, cuadrado o triángulo): ").lower()

if figura == "círculo" or figura == "circulo":
    radio = float(input("Introduce el radio: "))
    area = calcular_area(figura, radio=radio)
elif figura == "cuadrado":
    lado = float(input("Introduce el lado: "))
    area = calcular_area(figura, lado=lado)
elif figura == "triángulo" or figura == "triangulo":
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    area = calcular_area(figura, base=base, altura=altura)

print(area)

"""4. Contador de vocales
Crea una función contar_vocales que recibe una cadena de texto y devuelve cuántas vocales tiene. 
Luego, pide una frase al usuario y muestra el número de vocales utilizando la función."""

def contar_vocales(frase):
    vocales = 0
    for i in frase:
        if i in "aeiouAEIOU":
            vocales += 1
    return vocales

frase = input("Introduce una frase: ")
total_vocales = contar_vocales(frase)


print(total_vocales)

"""5. Número perfecto
Un número perfecto es aquel cuya suma de sus divisores (excluyendo el propio número) es igual al número. 
Crea una función llamada es_perfecto que determine si un número es perfecto o no."""

def es_perfecto(num1):
    suma_divisores = 0
    for i in range(1, num1):
        if num1 % i == 0:
            suma_divisores += i
    return suma_divisores == num1

num1 = int(input("Introduce el número: "))

if es_perfecto(num1):
    print("El número es perfecto.")
else:
    print("El número no es perfecto.")

"""6. Generador de tablas de multiplicar
Escribe una función tabla_multiplicar que reciba un número y muestre su tabla de multiplicar del 1 al 10. 
Pide un número al usuario y muestra su tabla usando la función."""

def tabla_multiplicar(num2):
    for i in range(1, 11):
        resultado_multiplicar = num2 * i
        print(num2, "*", i, "=", resultado_multiplicar)

num2 = int(input("Introduce el número: "))
tabla_multiplicar(num2)

"""7. Inversor de cadena
Crea una función llamada invertir_cadena que recibe una cadena y devuelve la cadena invertida. 
Luego, pide una frase al usuario y muestra el resultado."""

def invertir_cadena(frase):
    return frase[::-1]

frase = input("Introduce la frase: ")

resultado1 = invertir_cadena(frase)
print(resultado1)

"""8. Verificación de contraseña
Escribe una función verificar_contraseña que reciba una contraseña y verifique si cumple las siguientes condiciones:

Al menos 8 caracteres.
Contiene mayúsculas y minúsculas.
Contiene al menos un número.
Luego, pide una contraseña al usuario y verifica si es válida o no."""

def verificar_contraseña(contraseña):
    if len(contraseña) < 8:
        return "Contraseña no válida."
    
    tiene_mayúscula = False
    tiene_minúscula = False
    tiene_número = False
    
    for letra in contraseña:
        if letra.isupper():
            tiene_mayúscula = True
        elif letra.islower():
            tiene_minúscula = True
        elif letra.isdigit():
            tiene_número = True
    
    if tiene_mayúscula and tiene_minúscula and tiene_número:
        return "Contraseña válida."
    else:
        return "Contraseña no válida: debe tener mayúsculas, minúsculas y al menos un número."

contraseña = input("Introduce una contraseña: ")

resultado = verificar_contraseña(contraseña)
print(resultado)