def increment(x):
    return x + 1

def high_order(x, func): #func es una función que se pasa como argumento
    return x + func(x)

result = high_order(2, increment) #note que no se inicializa la función solo se pasa como argumento
print(result) # 5

increment_v2 = lambda x: x + 1 #función anónima

high_order_v2 = lambda x, func: x + func(x)
result_v2 = high_order_v2(2, increment_v2) #note que no se inicializa la función solo se pasa como argumento
print(result_v2)
result_v2 = high_order_v2(2, lambda x: x * 3) #note que no se inicializa la función solo se pasa como argumento
print(result_v2)