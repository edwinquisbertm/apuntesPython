numbers = { 1: "uno", 2: "dos", 3: "tres" } # diccionario con 3 elementos (clave: valor)
print(numbers[1]) # uno

information = { "name": "Juan", "age": 25, "city": "Bogotá" } # diccionario con 3 elementos (clave: valor)
print(information["age"]) # 25
del information["city"] # elimina el elemento con clave "city"
print(information) # {'name': 'Juan', 'age': 25}

claves = information.keys() # obtiene las claves del diccionario
print(claves) # dict_keys(['name', 'age'])
print(type(claves)) # <class 'dict_keys'>

values = information.values() # obtiene los valores del diccionario
print(values) # dict_values(['Juan', 25])

pairs = information.items() # obtiene las parejas clave-valor del diccionario
print(pairs) # dict_items([('name', 'Juan'), ('age', 25)])

contacto = {
    "juan": { "nombre": "Juan", "edad": 25, "ciudad": "Bogotá" },
    "ana": { "nombre": "Ana", "edad": 30, "ciudad": "Medellín" },
    "pedro": { "nombre": "Pedro", "edad": 35, "ciudad": "Cali" },
    } 
print(contacto["ana"]["edad"]) # 30
print(contacto["pedro"]) # {'nombre': 'Pedro', 'edad': 35, 'ciudad': 'Cali'}