def find_volume(length = 5, width = 1, depth = 2):
    return length * width * depth, width, 'hola' # podemos devolver varios valores en una función separados por comas y se devuelven en una tupla

'''result = find_volume(width=10) # podemos cambiar el valor de width sin cambiar el de length y depth al tener valores por defecto

print(result[2])'''

result, width, text = find_volume(width=20) # con esta forma podemos asignar los valores devueltos a variables separadas y no tener que acceder a ellos por índice en la tupla

print(result)
print(width)
print(text)