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

    # Cambiar el estado a False si el libro está disponible, y mostrar un mensaje si ya está prestado
    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            print(f"El libro {self.__titulo} ha sido prestado correctamente.")
        elif self.__disponible == False: 
            print(f"El libro {self.__titulo} no está disponible.")

    # Cambiar el estado de disponible a True si estaba prestado, y mostrar un mensaje si ya estaba disponible
    def devolver(self):
        if self.__disponible == False:
            self.__disponible = True
            print(f"El libro {self.__titulo} se ha devuelto correctamente.")
        elif self.__disponible:
            print(f"El libro ya estaba disponible en nuestra biblioteca.")

    # Mostrar los datos de un libro
    def mostrar(self):
        estado = "Disponible" if self.__disponible else "No disponible."
        return f"Título: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}, Disponible: {estado}"

    # Introducir un nuevo libro con sus características
    @staticmethod
    def agregar(biblioteca, titulo, autor, isbn):
        nuevo_libro = Libro(titulo, autor, isbn)
        biblioteca.append(nuevo_libro)
        print(f"El libro {titulo} ha sido agregado correctamente.")

    # Buscar un libro por su ISBN y mostrar sus datos
    @staticmethod
    def buscar(biblioteca, isbn):
        for libro in biblioteca:
            if libro.__isbn == isbn:
                print(libro.mostrar())
                return libro
        print("No disponemos de ese libro en nuestra biblioteca, disculpe las molestias.")
        return None

# Devolver una lista con todos los libros de la biblioteca y mostrar sus datos
def mostrar_todos_libros(biblioteca):
    if biblioteca:
        for libro in biblioteca:
            print(libro.mostrar())
    else:
        print("No hay libros registrados en la biblioteca.")

# Función principal que gestiona el menú de la biblioteca
def main():

    # Lista de libros
    biblioteca = []

    # Menu de la biblioteca
    while True:
        print("a) Agregar un nuevo libro.")
        print("b) Prestar un libro.")
        print("c) Devolver un libro.")
        print("d) Mostrar todos los libros.")
        print("e) Salir del programa.")
        option = input("Seleccione una opción, por favor: ").lower()

        if option == "a":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            Libro.agregar(biblioteca, titulo, autor, isbn)

        elif option == "b":
            isbn = input("Introduzca el ISBN del libro deseado: ")
            libro = Libro.buscar(biblioteca, isbn)
            if libro:
                libro.prestar()
            else:
                print(f"No se encontró ningún libro con ISBN: {isbn}")
        
        elif option == "c":
            isbn = input("Introduzca el ISBN del libro a devolver: ")
            libro = Libro.buscar(biblioteca, isbn)
            if libro:
                libro.devolver()
            else:
                print(f"No se encontró ningún libro con ISBN: {isbn}")

        elif option == "d":
            print(mostrar_todos_libros(biblioteca))

        elif option == "e":
            print("Saliendo del programa, gracias por su visita.")
            break
        
        else: 
            print("Opción no válida, por favor vuelva a introducir una opción.")

if __name__ == "__main__":
    main()
