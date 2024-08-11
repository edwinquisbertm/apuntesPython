matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix[0][0])  # 1

numbers = (1, 2, 3, 4, 5) # Tupla son inmutables
print(numbers)
print(type(numbers))
print(numbers[0])  # 1
numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment