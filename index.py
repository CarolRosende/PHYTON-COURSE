nombre="hola"
apellido="dos"

#Comentario

"""Comentario
de varias líneas"""

#Los datos conseguidos por input() siempre seran strg.

sg_nombre = input("Introduzca su nombre: ")
print("Bienvenido:", sg_nombre)

ng_edad = int(input("Introduzca su edad: "))
print("El año que viene, usted tendrá", ng_edad + 1, "años. Felicidades", sg_nombre, "!")

sg_nota = int(input("Introduce tu nota: "))

if sg_nota >= 5:
    print("Enhorabuena.")
else:
    print("Vuelve a intentarlo.")