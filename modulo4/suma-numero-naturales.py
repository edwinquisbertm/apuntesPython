# suma de numeros naturales

def suma_naturales(n):
    if (n == 0):
        return 0
    else:
        return n + suma_naturales(n - 1)

numero = int(input("Ingrese un número: "))
print("La suma de los primeros", numero, "números naturales es:", suma_naturales(numero)) # 3
