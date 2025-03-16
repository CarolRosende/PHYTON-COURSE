"""Ejercicio 1: Condicional básico
Escribe un programa que pida al usuario un número y determine si es positivo, negativo o cero. Luego, muestra un mensaje indicando el resultado.

Ejemplo de salida:
Ingresa un número: 5
El número es positivo."""

# Solicitar el número a ingresar.
ng_numero = int(input("Ingresa un número: "))

# Determinar si el número es positivo, negativo o cero.
if ng_numero>0:
    print(f"El número {ng_numero} es positivo.")
elif ng_numero<0:
    print(f"El número {ng_numero} es negativo.")
else:
    print(f"El número {ng_numero} es cero.")



"""Ejercicio 2: Comparación de números
Escribe un programa que pida al usuario dos números y determine cuál es el mayor, o si son iguales. Muestra un mensaje con el resultado.

Ejemplo de salida:
Ingresa el primer número: 10
Ingresa el segundo número: 20
El segundo número (20) es mayor que el primero (10)."""

# Solicitar al usuario que ingrese dos números.
ng_numero1 = int(input("Ingrese un número: "))
ng_numero2 = int(input("Ingrese otro número: "))

# Determinar cuál es mayor o si son iguales.
if ng_numero1 > ng_numero2:
    print(f"El número {ng_numero1} es mayor que el número {ng_numero2}")
elif ng_numero2 > ng_numero1:
    print(f"El número {ng_numero2} es mayor que el número {ng_numero1}")
else:
    print(f"Los números {ng_numero1} y {ng_numero2} son iguales")

"""Ejercicio 3: Par o impar
Escribe un programa que pida al usuario un número y determine si es par o impar. Muestra un mensaje con el resultado.

Ejemplo de salida:
Ingresa un número: 7
El número 7 es impar."""

# Solicitar al usuario que ingrese un número.
ng_numero3 = int(input("Introduce un número: "))

# Determinar si es par o impar.
if ng_numero3 % 2 == 0:
    print(f"El número {ng_numero3} es par.")
else:
    print(f"El número {ng_numero3} es impar.")


"""Ejercicio 4: Edad para votar
Escribe un programa que pida al usuario su edad y determine si es mayor de edad para votar (asumamos que la edad mínima para votar es 18 años). Muestra un mensaje indicando si puede votar o no.

Ejemplo de salida:
Ingresa tu edad: 16
No puedes votar, necesitas tener al menos 18 años."""

# Solicitar la edad del usuario.
ng_edad = int(input("Introduce tu edad: "))

# Determinar si es mayor de edad, y por lo tanto, puede votar.
if ng_edad >= 18:
    print(f"Enhorabuena! Al tener {ng_edad} puedes votar.")
else:
    print(f"Lo siento. Al tener {ng_edad} no puedes votar.")


"""Ejercicio 5: Calculadora simple
Escribe un programa que pida al usuario dos números y una operación (suma, resta, multiplicación o división). Luego, realiza la operación seleccionada y muestra el resultado. Si el usuario ingresa una operación no válida, muestra un mensaje de error.

Ejemplo de salida:
Ingresa el primer número: 10
Ingresa el segundo número: 5
Ingresa la operación (+, -, *, /): *
El resultado es: 50"""

# Solicitar los dos números y la operación.
ng_numero4 = int(input("Ingresa el primer número: "))
ng_numero5 = int(input("Ingresa el segundo número: "))
sg_operacion = input("Ingresa la operación(+, -, *, /): ")

# Realizar la operación y mostrar el resultado.
if sg_operacion == "+":
    print(f"El resultado es {ng_numero4 + ng_numero5}")
elif sg_operacion == "-":
    print(f"El resultado es {ng_numero4 - ng_numero5}")
elif sg_operacion == "*":
    print(f"El resultado es {ng_numero4 * ng_numero5}")
elif sg_operacion == "/":
    if ng_numero5 != 0:
        print(f"El resultado es {ng_numero4 / ng_numero5}")
    else:
        print("No es posible dividir entre 0.")
else:
    print("La operación no es válida.")


"""Ejercicio 6: Días de la semana
Escribe un programa que pida al usuario un número del 1 al 7 y muestre el día de la semana correspondiente (1 = Lunes, 2 = Martes, etc.). Si el número no está en ese rango, muestra un mensaje de error.

Ejemplo de salida:
Ingresa un número del 1 al 7: 3
El día correspondiente es Miércoles."""

# Solicitar un número del 1 al 7.
ng_numero6 = input("Introduce un número del 1 al 7: ")

# Determinar el día de la semana correspondiente:
if ng_numero6 == "1":
    print(f"El número {ng_numero6} es el día lunes.")
elif ng_numero6 == "2":
    print(f"El número {ng_numero6} es el día martes.")
elif ng_numero6 == "3":
    print(f"El número {ng_numero6} es el día miércoles.")
elif ng_numero6 == "4":
    print(f"El número {ng_numero6} es el día jueves.")
elif ng_numero6 == "5":
    print(f"El número {ng_numero6} es el día viernes.")
elif ng_numero6 == "6":
    print(f"El número {ng_numero6} es el día sábado.")
elif ng_numero6 == "7":
    print(f"El número {ng_numero6} es el día domingo.")
else:
    print("Error.")


"""Ejercicio 7: Año bisiesto
Escribe un programa que pida al usuario un año y determine si es bisiesto o no. Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400. Muestra un mensaje con el resultado.

Ejemplo de salida:Ingresa un año: 2020
El año 2020 es bisiesto."""

# Socilitar un año.
ng_año = int(input("Ingrese un año: "))

# Determinar si es bisiesto o no.
if (ng_año % 4 == 0 and ng_año % 100 != 0) or (ng_año % 400 == 0):
    print(f"{ng_año} es un año bisiesto")
else:
    print(f"{ng_año} no es un año bisiesto")


"""Un almacén da un descuento del 15% si la compra del cliente supera los 1000 Euros. 
Escribe un programa que pida el total de la compra y calcule el descuento 
(si aplica) y el total a pagar."""

# Solicitar el total de la compra.
ng_compra = float(input("Ingrese el total de la compra: €"))


# Determinar si se aplica el descuento y el total a pagar.
if ng_compra > 1000:
    total_descontado = round(ng_compra * 0.85, 2)
    print(f"El total de la compra, una vez aplicado el descuento, es {total_descontado}€")
else:
    print(f"El total a pagar es {round(ng_compra, 2)}€")


"""Escribe un programa que pida la edad del usuario y clasifique a las personas en diferentes categorías (niño, adolescente, adulto, adulto mayor). Supón los siguientes rangos de edad:

Niño: Menos de 13 años.
Adolescente: De 13 a 19 años.
Adulto: De 20 a 64 años.
Adulto mayor: 65 años o más."""

# Pedir la edad.
edad = int(input("Introduzca su edad: "))

# Clasificar en diferentes categorías.
if edad < 13:
    print("Eres un niño.")
else:
    if edad < 19:
        print("Eres un adolescente.")
    else:
        if edad < 64:
            print("Eres un adulto.")
        else:
            print("Eres un adulto mayor.")

"""Escribe un programa que sugiera qué ponerse basado en la temperatura actual 
(en grados Celsius) que el usuario introduce. Considera:

Menos de 10°C: Abrigo y bufanda.
De 10°C a 20°C: Suéter ligero.
Más de 20°C: Camiseta."""

# Pedir temperatura.
temperatura = int(input("Introduce la temperatura: "))

# Sugerencia de ropa.
if temperatura < 10:
    print("Deberías ponerte un abrigo o bufanda.")
else:
    if temperatura < 20:
        print("Deberías ponerte un suéter ligero.")
    else:
        if temperatura > 20:
            print("Deberías ponerte una camiseta.")
        else:
            print("Temperatura no válida.")