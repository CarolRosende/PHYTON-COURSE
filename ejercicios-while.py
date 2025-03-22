"""2. Contador de dígitos:
Pide un número al usuario y usa un while para contar cuántos dígitos tiene ese número."""

num = input("Introduce el número: ")

contador = 0

if num[0] == "-":
    num = num[1:]

while num != "":
    contador += 1
    num = num[:-1]

print("El número tiene", contador, "dígitos")


