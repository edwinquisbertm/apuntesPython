# conjuntos
# pueden modificar
# no se pueden repetir elementos
# no tienen orden

set_countries = {"Colombia", "Peru", "Chile", "Argentina", "Venezuela", "Ecuador"}
print(set_countries)
print(type(set_countries))

set_number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set_number)

set_types = {1, 2, 3, 4, False, 6, 7, 8, 9, 10, "Colombia", "Peru", "Chile", "Argentina", "Venezuela", "Ecuador"}

set_from_string = set("Colombia") # crea un conjunto con los caracteres de la cadena
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'as'))
print(set_from_tuples)

numbers = [1, 2, 3, 4, 5, 6, 3, 8, 9, 2]
set_numbers = set(numbers) # elimina los elementos repetidos
print(set_numbers)

unique_numbers = list(set_numbers) # convierte el conjunto en una lista
