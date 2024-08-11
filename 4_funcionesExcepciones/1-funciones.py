# def es la palabra reservada para definir una función los nombres de las funciones deben ser en minúsculas y separados por guiones bajos
def greet(name, last_name = "no tiene apellido"):
    print(name, last_name)
    
greet("angel", "villalba")
greet("diego") # si no se pasa el segundo argumento se toma el valor por defecto
greet(last_name="villalba", name="angel")

# calculadora
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator():
    while True:
        print("Seleccione una operación")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        input_option = int(input())
        if input_option == 1:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(add(a, b))
        elif input_option == 2:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(substract(a, b))
        elif input_option == 3:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(multiply(a, b))
        elif input_option == 4:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(divide(a, b))
        elif input_option == 5:
            print("Saliendo...")
            break
        else:
            print("Opción no válida")
            break
        
calculator()