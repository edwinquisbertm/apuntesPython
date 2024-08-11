for i in range(1, 10):
    print(i)
    
my_iter = iter(range(1, 3)) # iter() convierte un objeto en un iterable que se puede recorrer con un ciclo for  o con la función next() que permite acceder a los elementos de un iterable
print(my_iter)
print(next(my_iter)) # next() permite acceder a los elementos de un iterable
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) # StopIteration es un error que se lanza cuando se intenta acceder a un elemento que no existe