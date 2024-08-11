# funciones anónimas o lambda
# lambda argumentos: expresión

add = lambda a, b: a + b # función anónima que suma dos números a y b
print("suma:", add(1, 2))

mulitply = lambda a, b: a * b # función anónima que multiplica dos números a y b
print("Multiplicacion:", mulitply(2, 3))

# cuadrado de cada numero
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers)) # map aplica la función lambda a cada elemento de la lista numbers y devuelve una lista con los resultados
print("Cuadrado de cada número:", squared_numbers)

# filtrar números pares
event_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # filter devuelve una lista con los elementos de numbers que cumplen la condición de la función lambda
print("Números pares:", event_numbers)

# filtrar números impares
impar_numbers = list(filter(lambda x: x % 2 != 0, numbers)) # filter devuelve una lista con los elementos de numbers que cumplen la condición de la función lambda
print("Números impares:", impar_numbers)