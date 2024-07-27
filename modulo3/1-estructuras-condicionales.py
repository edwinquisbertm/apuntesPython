x = 5
# la identacion es importante en python y se usa para definir bloques de codigo dentro de una estructura condicional
if x > 5:
    print("x es mayor que 5")
elif x == 5: # elif es una abreviacion de else if
    print("x es igual a 5")
else:
    print("x es menor a 5")
    
print("este texto esta fuera de la estructura condicional")


a = 15
b = 20
# operadores logicos and y or
if a > 15 and b > 10:
    print("a es mayor a 15 y b es mayor a 10")
    
if a > 15 or b > 10:
    print("a es mayor a 15 o b es mayor a 10")
    
if not a > 15: # not es un operador de negacion
    print("a no es mayor a 15")
    

is_number = True
age = 15

if is_number:
    if age > 18:
        print("Tienes acceso ya que eres miembro, mayor a 18")
    else:
        print("No tienes ya que eres miembro menor a 18")
else:
    print("No eres miembro y NO TIENES ACCESO")