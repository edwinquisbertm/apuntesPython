'''
dictionary = {}
for i in range(1, 11):
    dictionary[i] = i * 2
    
print(dictionary)

dictionary_v2 = {i: i * 2 for i in range(1, 11)}
print(dictionary_v2)
'''
import random

countries = ['Mexico', 'Argentina', 'Colombia', 'Chile', 'Peru']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
    
print(population)

population_v2 = { country: random.randint(1, 100) for country in countries }
print(population_v2)

print("\n")

name = ['Juan', 'Pedro', 'Maria', 'Jose', 'Ana']
age = [12, 23, 34, 45, 56]
print(list(zip(name, age))) # para ver los elementos al utilizar zip en una lista de tuplas se convierte a lista, zip nos sirve para unir dos listas

new_dict = {name: age for name, age in zip(name, age)}

print(new_dict)