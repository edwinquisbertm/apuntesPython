to_do = ["Dirigirnos al hotel", "Ir a almorzar", "Visitar un museo", "Volver al hotel"]
print(to_do)

numbers = [1, 2, 3, 4, 5, "h"]
print(numbers)
print(type(numbers))
print(len(numbers))
print("primer elemento: ", numbers[0])
print("ultimo elemento: ", numbers[-1])# ultimo elemento se accede con el indice -1
string = "hola mundo"
print(to_do[0:2])# se imprime los elementos desde el indice 0 hasta el 2
print(to_do[1:])# se imprime los elementos desde el indice 1 hasta el final
print(to_do[:3])# se imprime los elementos desde el inicio hasta el indice 3
print(to_do[-2:])# se imprime los dos ultimos elementos
to_do.append("Volver a casa")# se agrega un elemento al final de la lista
print(to_do)
to_do.append(["otro", "elemento"])# se agrega una lista como un elemento
print(to_do)
to_do.insert(1, "Ir a cenar")# se agrega un elemento en la posicion 1
to_do.index("Ir a cenar")# se obtiene el indice de un elemento
print(to_do)
to_do.extend(["Ir a la playa", "Ir a la montaña"])# se agrega varios elementos al final de la lista
print(to_do)
to_do.remove("Ir a cenar")# se elimina un elemento
print(to_do)
to_do.pop()# se elimina el ultimo elemento
print(to_do)
to_do.pop(1)# se elimina el elemento en la posicion 1
print(to_do)
to_do.clear()# se eliminan todos los elementos
print(to_do)

numbers.max()# se obtiene el valor maximo
numbers.min()# se obtiene el valor minimo
numbers.sort()# se ordenan los elementos
print(numbers)
numbers.reverse()# se invierte el orden de los elementos
print(numbers)
numbers2 = numbers.copy()# se copia la lista
print(numbers2)
numbers3 = list(numbers)# se copia la lista
print(numbers3)
numbers4 = numbers# se copia la lista
print(numbers4)
numbers.append(6)
print(numbers)
