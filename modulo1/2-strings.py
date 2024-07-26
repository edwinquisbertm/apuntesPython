name = "Carlos"
otro = 'angel'
otra = '''hola 
mundo'''#cuando se usa triple comilla se puede escribir en varias lineas
print(type(name))
print(name)
print(otro)
print(otra)
print(name[0])
print(name + " "+ otro) #concatenar
print(4* name) #repetir
print(len(name)) #longitud
print(name.upper()) #mayusculas
print(name.lower()) #minusculas
print(name.replace('C','K')) #reemplazar
print(otra.split()) #separar
print(name.find('a')) #buscar
print(name.count('a')) #contar
print(name.isnumeric()) #es numerico
print(name.strip()) #quitar espacios