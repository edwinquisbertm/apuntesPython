#map: permite aplicar una función a cada elemento de una lista iterable (lista, tupla, etc.) y devuelve un iterador con los resultados.

numbers = [1, 2, 3, 4, 5]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)
    
numbers_v3 = map(lambda i: i * 2, numbers) # map para verlo como lista se debe convertir a lista
numbers_v4 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(list(numbers_v3))
print(numbers_v4)
print('\n\n')

numbers_5 = [1, 2, 3, 4]
numbers_6 = [5, 6, 7]

result = map(lambda x, y: x + y, numbers_5, numbers_6)
print(list(result))