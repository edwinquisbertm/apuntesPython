file = open('modulo10/text.txt')
#print(file.read()) # permite leer el contenido del archivo
''''
print(file.readline()) # permite leer la primera línea del archivo
print(file.readline())
print(file.readline()) '''

for line in file:
    print(line)

file.close() # cierra el archivo y libera los recursos

with open('modulo10/text.txt') as file: # abre el archivo y lo cierra automáticamente
    for line in file:
        print(line)