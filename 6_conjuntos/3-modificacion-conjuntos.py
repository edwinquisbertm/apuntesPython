#Funciones de set:
#add(): Añade un elemento.
#update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
#discard(): Elimina un elemento y si ya existe no lanza ningún error.
#remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
#pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
#clear(): Elimina todo el contenido del conjunto.

set_countries = {'Colombia', 'Peru', 'Chile', 'Argentina', 'Venezuela', 'Ecuador'}

size = len(set_countries) # obtiene el tamaño del conjunto
print(size)

print("Colombia" in set_countries) # verifica si un elemento esta en el conjunto
print("Mexico" in set_countries)

# add(): Añade un elemento.
set_countries.add("Mexico")
set_countries.add("Mexico")
print(set_countries)# no se pueden repetir elementos

#update
set_countries.update({"Brasil", "Uruguay", "Paraguay"})# añade varios elementos
print(set_countries)

#remove
set_countries.remove("Mexico")
print(set_countries)
#set_countries.remove("Mex") # lanza un error si el elemento no existe
set_countries.discard("Mex") # no lanza un error si el elemento no existe
print(set_countries)

set_countries.clear() # elimina todos los elementos del conjunto
print(len(set_countries))