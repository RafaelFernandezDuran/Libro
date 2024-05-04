# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if not libro.titulo or not libro.autor:
            raise ValueError("El libro debe tener un título y un autor.")
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        raise ValueError(f"No se encontró ningún libro con el título '{titulo}'.")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro.titulo} (Autor: {libro.autor}, Año: {libro.año_publicacion})")

class ErrorLibroSinTitulo(Exception):
    pass

class ErrorLibroSinAutor(Exception):
    pass

class MenuBiblioteca:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca

    def ejecutar(self):
        while True:
            print("\nMenú:")
            print("1. Agregar libro")
            print("2. Buscar libro por título")
            print("3. Mostrar todos los libros")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_libro()
            elif opcion == "2":
                self.buscar_libro()
            elif opcion == "3":
                self.biblioteca.mostrar_libros()
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        año_publicacion = input("Ingrese el año de publicación del libro: ")

        if not titulo:
            raise ErrorLibroSinTitulo("El libro debe tener un título.")
        if not autor:
            raise ErrorLibroSinAutor("El libro debe tener un autor.")

        libro = Libro(titulo, autor, año_publicacion)
        self.biblioteca.agregar_libro(libro)

    def buscar_libro(self):
        titulo = input("Ingrese el título del libro a buscar: ")
        try:
            libro_encontrado = self.biblioteca.buscar_libro(titulo)
            print(f"Libro encontrado: {libro_encontrado.titulo} (Autor: {libro_encontrado.autor}, Año: {libro_encontrado.año_publicacion})")
        except ValueError as e:
            print(e)

def main():
    biblioteca = Biblioteca()
    menu = MenuBiblioteca(biblioteca)
    menu.ejecutar()

if __name__ == "__main__":
    main()
