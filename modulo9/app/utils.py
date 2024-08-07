def get_population():
    keys = ['name', 'population', 'area']
    values = ['San Francisco', 884363, 231.89]
    return keys, values

A = 'Hola'

def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result


    
