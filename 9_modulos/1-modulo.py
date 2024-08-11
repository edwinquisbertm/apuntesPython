import sys
#print(sys.path) # Imprime una lista con los directorios donde Python buscará los módulos que importemos

import re
# El módulo re nos permite trabajar con expresiones regulares en Python
text = "Hola, soy edwin y mi calle es 1234 y mi celular es 1234567890"
result = re.findall('[0-9]+', text)
#print(result) # Imprime ['1234', '1234567890']

import time
# El módulo time nos permite trabajar con fechas y horas en Python
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(timestamp) # Imprime un número que representa la cantidad de segundos desde el 1 de enero de 1970
print('\n', result, '\n') # Imprime la fecha y hora actual

import collections
# El módulo collections nos permite trabajar con colecciones de datos en Python como ser diccionarios, listas, tuplas, etc.
numbers = [1, 2, 1, 2, 1, 3, 4, 5, 4, 5, 4, 6, 7, 8, 7, 8, 7, 9, 10, 9, 10]
counter = collections.Counter(numbers)
print(counter) # Imprime Counter({1: 3, 2: 2, 4: 3, 7: 3, 5: 2, 9: 2, 3: 1, 6: 1, 8: 1, 10: 1})


