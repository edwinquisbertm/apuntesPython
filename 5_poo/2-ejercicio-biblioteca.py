class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestamo(self):
        if self.disponible:
            self.disponible = False
            print(f'El libro {self.titulo} ha sido prestado')
        else:
            print(f'El libro {self.titulo} no esta disponible')
            
    def devolucion(self):
        if self.disponible:
            print(f'El libro {self.titulo} ya esta disponible')
        else:
            self.disponible = True
            print(f'El libro {self.titulo} ha sido devuelto')
            
class User:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []
        
    def prestar_libro(self, libro):
        if libro.disponible:
            libro.prestamo()
            self.libros_prestados.append(libro)
        else:
            print(f'El libro {libro.titulo} no esta disponible')
            
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.devolucion()
            self.libros_prestados.remove(libro)
        else:
            print(f'El libro {libro.titulo} no ha sido prestado por {self.nombre}')
            
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'El libro {libro.titulo} ha sido agregado a la biblioteca')
        
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f'El usuario {usuario.nombre} ha sido agregado a la biblioteca')
        
    def mostrar_libros_disponibles(self):
        print('Libros disponibles:')
        for libro in self.libros:
            if libro.disponible:
                print(f'{libro.titulo} - {libro.autor}')
        
# Crear libros
book1 = Libro('El principito', 'Antoine de Saint-Exupéry')
book2 = Libro('El señor de los anillos', 'J.R.R. Tolkien')
book3 = Libro('Harry Potter', 'J.K. Rowling')
book4 = Libro('Cien años de soledad', 'Gabriel García Márquez')
book5 = Libro('Don Quijote de la Mancha', 'Miguel de Cervantes')
book6 = Libro('La Odisea', 'Homero')

# Crear usuarios
user1 = User('John', 1)
user2 = User('Jane', 2)
user3 = User('Alice', 3)

# Crear biblioteca
biblioteca = Biblioteca()
biblioteca.agregar_libro(book1)
biblioteca.agregar_libro(book2)
biblioteca.agregar_libro(book3)
biblioteca.agregar_libro(book4)
biblioteca.agregar_libro(book5)
biblioteca.agregar_libro(book6)

biblioteca.agregar_usuario(user1)
biblioteca.agregar_usuario(user2)
biblioteca.agregar_usuario(user3)

# mostrar libros disponibles
biblioteca.mostrar_libros_disponibles()

# realizar prestamos
user1.prestar_libro(book1)

biblioteca.mostrar_libros_disponibles()

user1.devolver_libro(book1)