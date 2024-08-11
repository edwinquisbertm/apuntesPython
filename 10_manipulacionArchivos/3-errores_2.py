try: # sirve para capturar errores en tiempo de ejecución y manejarlos de una forma controlada sin que el programa se detenga
    print(0 / 0)
except ZeroDivisionError as error: # ZeroDivisionError es un error que se lanza cuando se intenta dividir un número por cero
    print(error)

print('hola')

try:
    assert 1 != 1, '1 es igual a 1' # AssertionError es un error que se lanza cuando una afirmación falla
except AssertionError as error:
    print(error)
    
print('hola2')

try:
    age = 10
    if age < 18:
        raise Exception('Menores de edad no pueden acceder a este sitio') # Exception es un error que se lanza cuando se produce una excepción en el código
except Exception as error:
    print(error)
    
print('hola3')

print('\n')

try:
    print(0 / 0)
    assert 1 != 1, '1 es igual a 1'
    age = 10
    if age < 18:
        raise Exception('Menores de edad no pueden acceder a este sitio')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)
    
print('hola3')

'''
try:
    pass
except Exception as e:
    raise
else:
    pass
finally:
    pass
'''