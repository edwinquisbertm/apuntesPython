'''
Los permisos de lectura y escritura se pueden combinar con el signo +.
los permisos se definen de la siguiente manera:
r+ : lectura y escritura
w+ : escritura y lectura
a+ : escritura y lectura, pero el archivo se abre en modo de adición
r : lectura
w : escritura
a : escritura, pero el archivo se abre en modo de adición
'''

with open ('modulo10/text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nHello, World!')