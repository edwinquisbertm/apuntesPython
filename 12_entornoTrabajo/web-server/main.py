import store
from fastapi import FastAPI # Importamos la librería fastAPI y la renombramos como fastAPI para poder usarla
from fastapi.responses import HTMLResponse

app = FastAPI() # Creamos una instancia de FastAPI

@app.get('/') # Definimos una ruta para el método GET
def get_list():
    return [1, 2, 3, 4, 5]

@app.get('/contact', response_class = HTMLResponse) # Definimos una ruta para el método GET y especificamos que la respuesta será HTML
def get_list():
    return """
        <html>
            <head>
                <title>Contact</title>
            </head>
            <body>
                <h1>Contact</h1>
                <p>Send us an email to <a href="mailto: ""> </a></p>
            </body>
        </html>
    """

def run():
    store.get_categories()
    
if __name__ == '__main__':
    run()