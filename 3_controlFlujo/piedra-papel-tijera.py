import random
contrincante = random.choice(["piedra", "papel", "tijera"])
user = input("¿piedra, papel o tijera? ")

if (user == "piedra" and contrincante == "tijera"):
    print("Ganaste, la computadora eligio tijera")
elif user == "piedra" and contrincante == "papel":
        print("Perdiste, la computadora eligio papel")
elif (user == "papel" and contrincante == "piedra"):
    print("Ganaste, la computadora eligio piedra")
elif user == "papel" and contrincante == "tijera":
        print("Perdiste, la computadora eligio tijera")
elif (user == "tijera" and contrincante == "papel"):
    print("Ganaste, la computadora eligio papel")
elif user == "tijera" and contrincante == "piedra":
        print("Perdiste, la computadora eligio piedra")
else:
    print("Empate")
        
print("fin del juego")