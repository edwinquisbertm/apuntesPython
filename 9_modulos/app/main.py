import utils

keys, values = utils.get_population()
print(keys, values)

print(utils.A)

data = [
    {'Country': 'Mexico', 'Population': 126190788},
    {'Country': 'USA', 'Population': 331002651},
    {'Country': 'Canada', 'Population': 37742154}
]
def run():

    country = input('Enter a country: ')

    result = utils.population_by_country(data, country)
    print(result)
    
if __name__ == '__main__': # este bloque se ejecuta si el script se ejecuta directamente y no si se importa como modulo en otro script
    run()