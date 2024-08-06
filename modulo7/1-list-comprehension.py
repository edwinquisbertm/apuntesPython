'''
numbers = []
for element in range(1, 11):
    numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1, 11)] #List comprehension para crear una lista de 1 a 10 en una sola línea
print(numbers_v2)
'''

numbers = []
for element in range(1, 11):
    if element % 2 == 0:
        numbers.append(element * 2)

print(numbers)

numbers_v3 = [element * 2 for element in range(1, 11) if element % 2 == 0] #List comprehension para crear una lista de 1 a 10 en una sola línea con condicional donde solo se agregan los números pares
print(numbers_v3)