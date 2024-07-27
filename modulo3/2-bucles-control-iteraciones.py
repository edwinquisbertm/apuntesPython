numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print("i es igual a: ", i+2)
    
for i in range(10): # range(10) genera una lista de 10 elementos [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("i es igual a: ", i)
    
fruits = ["apple", "banana", "cherry", "orange"]

for fruta in fruits:
    print("La fruta es: ", fruta)
    if fruta == "banana":
        print("encontramos la banana")
        break # break termina el bucle

x = 0
while x < 10:
    print("x es igual a: ", x)
    x += 1
    if x == 3:
        break
    
