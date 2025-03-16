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



