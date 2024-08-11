#Tipos de Errores

'''
print(0 / 0) # ZeroDivisionError es un error que se lanza cuando se intenta dividir un número por cero

# print(4 + spam*3) # NameError es un error que se lanza cuando se intenta acceder a una variable que no ha sido definida

# print('2' + 2) # TypeError es un error que se lanza cuando se intenta realizar una operación con dos tipos de datos incompatibles

suma = lambda x, y: x + y
assert suma(2, 2) == 4 # Assertion es una afirmación que se utiliza para verificar si una condición es verdadera, si la condición es falsa se lanza un AssertionError
suma = lambda x, y: x + y * 2
assert suma(2, 2) == 4 # AssertionError es un error que se lanza cuando una afirmación falla

age = 10
if age < 18:
    raise Exception('Menores de edad no pueden acceder a este sitio') # Exception es un error que se lanza cuando se produce una excepción en el código
'''