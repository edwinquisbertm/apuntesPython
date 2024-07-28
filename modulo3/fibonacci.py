# Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fibonacci(limit):
    a, b = 0, 1 # asignamos los valores iniciales en una sola linea
    while a < limit:
        yield a # yield es una palabra reservada que se usa para retornar un valor en una funcion generadora
        a, b = b, a + b
        # a, b = b, a + b esto significa que a = b y b = a + b en una sola linea de codigo
for value in fibonacci(50):
    print(value)