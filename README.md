# apuntesPython
Ruta de aprendizaje de Python

# Libros de Apoyo
https://www3.uji.es/~vjimenez/AULASVIRTUALES/PL-0910/python-by-vilar.pdf

# Lecturas recomendadas
https://es.wikipedia.org/wiki/Orden_de_evaluaci%C3%B3n

https://docs.python.org/es/3/library/stdtypes.html#string-methods

https://docs.python.org/3/library/dataclasses.html

https://es.wikipedia.org/wiki/Zen_de_Python

https://replit.com/@NicolasMolina13/Python-102#main.py

https://elpythonista.com/zen-de-python

https://www.w3schools.com/python/python_ref_set.asp

https://www.geeksforgeeks.org/difference-between-list-vs-set-vs-tuple-in-python/

https://www.kaggle.com/

https://www.w3schools.com/python/python_file_open.asp

https://platzi.com/blog/matplotlib/

https://matplotlib.org/

https://www.w3schools.com/python/matplotlib_pyplot.asp

# configuracion de entorno de trabajo profesional

Comandos Utilizados

python

python3

exit() para salir de la interfaz de python

Instalación

apt update

sudo apt update

sudo apt -y upgrade

Verificar Instalación de python

python3 -V
Instalación de gestor de paquetes de dependencias

sudo apt insstall -y python3-pip
Verificar Instalación del gestor

pip3 -V
Dependencias en entorno profesional

apt install -y build-essential libssl-dev libffi-dev python3-dev

# instalacion de paquetes
https://pypi.org/

# virtualizar un entorno de trabajo

- Crear entorno virtual con el nombre venv:
python3 -m venv venv

- Activar entorno virtual:
source venv/bin/activate

- pip freeze para verificar que no ha nada instalado:
pip freeze

- Instalar:
pip install matplotlib

- pip freeze para verificar lo instalado solo en el entorno virtual:
pip freeze

- para desactivar el entorno virtual
deactivate

- Verificar donde esta python y pip

which python3

which pip3

- Si estas en linus o wsl debes instalar

sudo apt install -y python3-venv

- Poner cada proyecto en su propio ambiente, entrar en cada carpeta.

python3 -m venv env

- Activar el ambiente

source env/bin/activate

- Salir del ambiente virtual

deactivate

- Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo

pip3 install matplotlib==3.5.0

- Verificar las instalaciones

pip3 freeze

# requirements.txt
- para crearlo usamos:
pip3 freeze > requirements.txt

- para instalarlo
pip3 install -r requirements.txt 

# Lecturas de request
https://requests.readthedocs.io/en/latest/

# Api de practica platzi
https://fakeapi.platzi.com/

https://fastapi.tiangolo.com/#installation

https://fastapi.tiangolo.com/advanced/custom-response/#html-response

# instalar fastapi
pip3 install fastapi
pip3 install "fastapi[standard]"
pip3 install 'uvicorn[standard]'

https://www.uvicorn.org/

# inicio del servidor
uvicorn main:app --reload
uvicorn main:app

fastapi dev main.py

# Contendores con Docker
nos permiten controlar la version del lenguaje  y poder moverlo entre entornos de trabajo

https://docs.docker.com/desktop/install/windows-install/

- para compilar el contenedor de docker:
docker-compose build 

- para inicializar el contenedor de docker enviamos
docker-compose up -d

- para ejecutar el contenedor de docker
docker-compose exec app-csv bash

# cambios en el codigo con docker
Cuando realizar cambios en el codigo este cambio no se aplica al contenedor creado por lo que debemos volver a ejecutar:

docker-compose build

docker-compose up -d

docker-compose exec app-csv bash

# Otra forma de enlazar el contenedor a los cambios en el codigo es utilizan el archivo docker-compose.yml
En este agregaremo la propiedad columes en el que indicaremos que el el directorio esta enlazado al contenedor para que de esa forma los cambios esten conectados

# comprobar si esta corriendo docker
docker-compose ps