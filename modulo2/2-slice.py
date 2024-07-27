a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = a
print(a)
print(b)

del a[0] # se elimina el primer elemento de la lista de ambas variables porque ambas variables apuntan a la misma direccion de memoria
print(id(a))
print(id(b))

c = a[:] # se copia la lista en diferentes direcciones de memoria
print(id(c))
print(id(a))