# concesionaria de autos
# debe poder realizarse la compra y venta de autos, ademas de mostrar los autos disponibles, precio y poder comprar uno

class Auto:
    def __init__ (self, modelo, precio):
        self.modelo = modelo
        self.precio = precio
        self.disponible = True
    
    def venta(self):
        if self.disponible:
            self.disponible = False
            print(f'El auto {self.modelo} ha sido vendido')
        else:
            print(f'El auto {self.modelo} no esta disponible')
            
    def devolucion(self):
        if self.disponible:
            print(f'El auto {self.modelo} ya esta disponible')
        else:
            self.disponible = True
            print(f'El auto {self.modelo} ha sido devuelto')
            
            
class Cliente:
    def __init__(self, nombre, cliente_id):
        self.nombre = nombre
        self.cliente_id = cliente_id
        self.autos_comprados = []
        
    def comprar_auto(self, auto):
        if auto.disponible:
            auto.venta()
            self.autos_comprados.append(auto)
        else:
            print(f'El auto {auto.modelo} no esta disponible')
            
    def devolver_auto(self, auto):
        if auto in self.autos_comprados:
            auto.devolucion()
            self.autos_comprados.remove(auto)
        else:
            print(f'El auto {auto.modelo} no ha sido comprado por {self.nombre}')
            
class Concesionaria:
    def __init__ (self):
        self.autos = []
        self.clientes = []
    
    def agregar_auto(self, auto):
        self.autos.append(auto)
        print(f'El auto {auto.modelo} ha sido agregado a la concesionaria')
        
    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f'El cliente {cliente.nombre} ha sido agregado a la concesionaria')
    
    def mostrar_autos_disponibles(self):
        print('Autos disponibles:')
        for auto in self.autos:
            if auto.disponible:
                print(f'{auto.modelo} - ${auto.precio}')
    
# Crear autos
auto1 = Auto('Fiat 500', 10000)
auto2 = Auto('Ford Fiesta', 15000)
auto3 = Auto('Chevrolet Onix', 20000)

# Crear clientes
cliente1 = Cliente('Juan', 1)
cliente2 = Cliente('Maria', 2)

# Crear concesionaria
concesionaria = Concesionaria()
concesionaria.agregar_auto(auto1)
concesionaria.agregar_auto(auto2)
concesionaria.agregar_auto(auto3)
concesionaria.agregar_cliente(cliente1)
concesionaria.agregar_cliente(cliente2)

# Mostrar autos disponibles
concesionaria.mostrar_autos_disponibles()

# Comprar autos
cliente1.comprar_auto(auto1)
cliente2.comprar_auto(auto2)

# Mostrar autos disponibles
concesionaria.mostrar_autos_disponibles()

# Devolver autos
cliente1.devolver_auto(auto1)

concesionaria.mostrar_autos_disponibles()