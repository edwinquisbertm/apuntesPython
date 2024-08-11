import random
countries = ['USA', 'China', 'India', 'Brazil', 'Pakistan', 'Nigeria', 'Bangladesh', 'Russia', 'Mexico', 'Japan']

population_v2 = { country: random.randint(1, 100) for country in countries }
print(population_v2, end='\n\n')

result = { country: population for (country, population) in population_v2.items() if population > 50 }

print('segundo resultado:\n', result)

text = 'Hola, soy thiago'

unique = { c: c.upper() for c in text if c in 'aeiou'}# si la letra esta en la cadena 'aeiou' la convierte a mayuscula
print(unique)
