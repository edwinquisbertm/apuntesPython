def increment(x):
    return x + 1

lambda x: x + 1

increment_v2 = lambda x: x + 1 # lambda function se asigna a una variable para poder ser llamada
result = increment(5)
print(result)
print(increment_v2(5))

full_name =  lambda name, last_name: f'hola soy {name.title()} {last_name.title()}' # title() se utiliza para que la primera letra de cada palabra sea mayúscula

print(full_name('Juan', 'Perez'))