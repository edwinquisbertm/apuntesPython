# operadores de entrada y salida
# entrada de datos por teclado con la funcion input() 

nombre = input("Cual es tu nombre? ")
print("Hola", nombre)
edad = input("Cual es tu edad? ") # la funcion input() devuelve un string
print("Edad: ", edad)

# salida de datos por pantalla con la funcion print()
print("Hola", nombre, "tu edad es: ", edad)
print(type(nombre))
print(type(edad))

# casting de datos con las funciones int(), float(), str()

edad = int(edad)
print("Edad: ", edad)
print(type(edad))

dia = int(input("Cual es tu dia de nacimiento? "))
print(type(dia))
print("Dia: ", dia)