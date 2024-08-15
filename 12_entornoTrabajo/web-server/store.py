import requests

def get_categories():
    response = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(response.status_code) # esta linea es para saber si la peticion fue exitosa
    #print(response.text) # esta linea es para ver la respuesta del servidor
    print(type(response.text)) # esta linea es para saber el tipo de dato que se esta recibiendo
    categories = response.json() # esta linea es para convertir el texto a un diccionario
    for category in categories:
        print(category['id'])
        print(category['name'])