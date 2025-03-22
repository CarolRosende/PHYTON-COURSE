# Crear la clase Libro
class Libro:
    # Crear los atributos
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__disponible = True

    # Crear getter para 'titulo'
    @property
    def titulo(self):
        return self.__titulo
    
    # Crear setter para 'titulo'
    @titulo.setter
    def titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    # Crear getter para 'autor'
    @property
    def autor(self):
        return self.__autor
    
    # Crear setter para 'autor'
    @autor.setter
    def autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    # Crear getter para 'isbn'
    @property
    def isbn(self):
        return self.__isbn
    
    # Crear setter para 'isbn'
    @isbn.setter
    def isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn
    
    # Crear getter para 'disponible'
    @property
    def disponible(self):
        return self.__disponible

    # Incluir un método que cambie el estado de disponible a False si el libro está disponible, y muestre un mensaje si ya está prestado
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El libro {self.__titulo} ha sido prestado correctamente.")
        elif self.__disponible == False: 
            print(f"El libro {self.__titulo} no está disponible.")

    # Incluir un método que cambie el estado de disponible a True si estaba prestado, y muestre un mensaje si ya estaba disponible.
    def devolver(self):
        if self.__disponible == False:
            self.__disponible = True
            print(f"El libro {self.__titulo} se ha devuelto correctamente.")
        elif self.__disponible:
            print(f"El libro ya estaba disponible en nuestra biblioteca.")

    # Incluir un método que devuelva una lista con todos los libros de la biblioteca y los muestre en pantalla con todos sus datos y diga si estás disponible o no.
    def mostrar(self):
        estado = "Disponible" if self.__disponible else "No disponible."
        return f"Título: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}, Disponible: {estado}"

    # Incluir un método que permita introducir un nuevo libro con sus características
    @staticmethod
    def agregar(biblioteca, titulo, autor, isbn):
        nuevo_libro = Libro(titulo, autor, isbn)
        biblioteca.append(nuevo_libro)
        print(f"El libro {titulo} ha sido agregado correctamente.")

    # Incluye un método que busque un libro en concreto por su ISBN y lo muestre en pantalla con todos sus datos y diga si está disponible o no.
    @staticmethod
    def buscar(biblioteca, isbn):
        for libro in biblioteca:
            if libro.__isbn == isbn:
                return libro
            else:
                print("No disponemos de ese libro en nuestra biblioteca, disculpe las molestias.")

biblioteca = []

Libro.agregar(biblioteca, "Paula", "Romeo", "3456")

Libro.buscar(biblioteca, "3456")

    
"""1. Clase Libro:

2. Gestión del inventario:
• Usa una lista para almacenar objetos de la clase Libro.
# Implementa un bucle que permita al usuario interactuar con el
programa mediante un menú con las siguientes opciones:
• a) Agregar un nuevo libro ingresando título, autor e ISBN.
• b) Prestar un libro buscando por ISBN.
• c) Devolver un libro buscando por ISBN.
• d) Mostrar todos los libros y su estado (disponible o no).
• e) Salir del programa.


3. Condiciones:
• Valida que el ISBN ingresado exista en la lista antes de prestar o
devolver un libro.
• Si el usuario ingresa una opción inválida en el menú, muestra un
mensaje de error y vuelve a pedir una opción."""
