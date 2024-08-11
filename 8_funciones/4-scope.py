'''El scope hace referencia al alcance de las variables en el programa. Así pues, una variable está disponible solo en la región en la que se crea.

Local scope. Este tipo de alcance lo tienen las variables declaradas al interior de una estructura, como una función, y pueden ser empleadas únicamente al interior de la misma.

Enclosing Scope. También conocido como Non-local Scope, se refiere a variables definidas en funciones anidadas; estas variables no son locales pero tampoco globales.

Global scope. Variables creadas en el cuerpo principal del código de Python y que pueden ser accedidas desde cualquier scope, global o local.

Built-in scope. Cuando una variable no se encuentra en ninguno de los scope anteriores, Python empieza a buscar en el built-in scope, el cual cubre todas las palabras reservadas del lenguaje. Pueden ser llamadas en cualquier lugar sin necesidad de ser definidas:'''

price = 100 # Global scope


def increment():
    price = 200 # Local scope
    result = price + 10 # Local scope, esta variable solo existe dentro de la función y no puede ser accedida desde fuera de la misma
    print(result)
    return result

print(price)
price_2 = increment()
print(price_2)