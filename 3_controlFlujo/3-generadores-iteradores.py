# Ejemplo de Iterador

# Crear una lista
my_list = [1, 2, 3, 4, 5]

# Obtenemos un iterador
my_iterador = iter(my_list)

# Usar el iterador
print(next(my_iterador)) # 1
print(next(my_iterador)) # 2
print(next(my_iterador)) # 3
print(next(my_iterador)) # 4
print(next(my_iterador)) # 5
print("Fin de la lista \n")

# iterar cadenas
text = "Hola Mundo"

iter_text = iter(text)

for char in iter_text:
    print(char)
    
# Crear un iterador para los numeros impares

limite = 10

add_itter = iter(range(1, limite+1, 2)) # estipulamos que empiece en 1 y que vaya de 2 en 2

for num in add_itter:
    print(num)
    
def my_generator():
    yield 1
    yield 2
    yield 3
    
for value in my_generator():
    print(value)