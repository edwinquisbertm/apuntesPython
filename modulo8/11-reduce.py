import functools # Importamos el módulo functools para poder usar la función reduce de Python

numbers = [1, 2, 3, 4, 5]
result = functools.reduce(lambda counter, item: counter + item, numbers) # Suma todos los elementos de la lista numbers y guarda el resultado en la variable result
# reduce necesita dos argumentos: una función y una lista en la funcion se le pasan dos argumentos, el primero es el acumulador y el segundo es el elemento de la lista

print(result) # Imprime 15
