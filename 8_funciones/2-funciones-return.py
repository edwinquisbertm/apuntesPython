def sum_with_range(min, max):
    print (min, max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum # return nos permite devolver un valor de la función para ser utilizado en otro lugar
    
result = sum_with_range(1, 10)
print(result, '\n')
result_2 = sum_with_range(result, result + 20)
print(result_2)