"""Par o impar:"""
numero = int(input("Introduce un número: "))

if numero % 2 == 0:
    print("Es par.")
elif numero % 2 != 0:
    print("Es impar.")
else:
    print("No válido.")

"""Adivina el número:
Genera un número aleatorio entre 1 y 10.
El usuario debe adivinarlo y recibir pistas de “mayor” o “menor” hasta acertar."""

import random
numero_azar = random.randint(1, 10)

numero_usuario = int(input("¿Qué número será?: "))

while numero_usuario != numero_azar:
    if numero_usuario < numero_azar:
        print("El número es mayor que el introducido.")
    else:
        print("El número es menor que el introducido.")
    
    numero_usuario = int(input("¿Qué número será?: "))

print("Adivinaste el número!")


"""Contador de vocales:
Pide una palabra e imprime cuántas vocales tiene."""

palabra = input("Introduce una palabra: ")

numero_vocales = 0

for letra in palabra:
    if letra in "aeiouAEIOU":
        numero_vocales += 1

print(numero_vocales)
    

"""Suma de los primeros N números:
Pide un número 𝑁 e imprime la suma de los números de 1 hasta 𝑁."""

numero2 = int(input("Introduce un número: "))

suma = 0

for i in range(1, numero2 + 1):
    suma += i

print(suma)

"""Contar números impares en un rango
Pide al usuario un número y cuenta cuántos números impares hay desde 1 hasta ese número (inclusive)."""

numero3 = int(input("Introduce el número: "))

impares = 0

for i in range(1, numero3 + 1):
    if i % 2 != 0:
        impares += 1

print(impares)

"""Determinar si un número es primo
Pide al usuario un número e indica si ese número es primo.
Pistas: Un número es primo si solo tiene dos divisores: 1 y él mismo. Usa un bucle que verifique los divisores posibles del número y un condicional para determinar si es primo"""

numero4 = int(input("Introduce el número: "))

es_primo = True

for i in range(2, numero4):
    if numero4 % i == 0:
        es_primo = False
        break

if es_primo:
    print(f"El número {numero4} es primo.")
else:
    print(f"El número {numero4} no es primo.")
