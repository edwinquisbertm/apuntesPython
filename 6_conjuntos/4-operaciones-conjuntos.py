'''Operaciones set
union(set): Realiza la operacion “union” entre dos conjuntos. La unión entre dos conjuntos es sumar los elementos de estos sin repetir elementos. Esta operación tambien se puede realizar con el signo “|”: set_a | set_b.

intersection(set): Realiza la operacion “intersection” entre dos conjuntos. La intersección entre dos conjuntos es tomar unicamente los elementos en común de los conjutnos. Esta operación tambien se puede realizar con el signo “&”: set_a & set_b.

difference(set): Realiza la operacion “difference” entre dos conjuntos. La diferencia entre dos conjuntos es restar los elementos del segundo conjunto al primero. Esta operación tambien se puede realizar con el signo “-”: set_a - set_b.

symmetric_difference(set): Realiza la operacion “symmetric_difference” entre dos conjuntos. La diferencia simetrica entre dos conjutnos consta de restar todos los elementos de ambos exceptuando el elemento en común. Esta operación tambien se puede realizar con el signo “^”: set_a ^ set_b.

NOTA: No se pueden realizar operaciones con otras colecciones de datos, solo se puede únicamente entre conjuntos.'''

set_a = {'morado', 'rojo', 'verde', 'azul'}
set_b= {'color', 'rojo', 'amarillo', 'naranja'}

#union
set_c = set_a.union(set_b) #une los dos conjuntos sin repetir elementos
print(set_c)
print(set_a | set_b)#union con el signo "|"

#Intersección
set_c = set_a.intersection(set_b) #solo muestra los elementos que se repiten
print(set_c)
set_c = set_a & set_b#Intersección con el signo "&"

#Diferencia
set_c = set_a.difference(set_b)#Resta los elementos del segundo conjunto al primero y muestra los elementos que quedan
print(set_c)
set_c = set_a - set_b#Diferencia con el signo "-"

#Diferencia simetrica
set_c = set_a.symmetric_difference(set_b)#une los dos conjuntos sin repetir elementos en común
print(set_c)
print(set_a ^ set_b)#Diferencia simetrica con el signo "^"