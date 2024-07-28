# Hallar el factorial de un numero
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 0! = 1
# 1! = 1

# Función recursiva para hallar el factorial de un número

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
factorial_5 = print(factorial(5)) # 120
factorial_0 = print(factorial(0)) # 1
print("fin de factorial\n")

# funcion recursiva fibonacci
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
fibonacci_5 = print("fibonacci: ", fibonacci(5)) # 5