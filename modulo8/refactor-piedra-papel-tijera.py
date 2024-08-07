import random

def obtener_contrincante():
    opciones = ['piedra', 'papel', 'tijera']
    return random.choice(opciones)

def obtener_ganador(jugador, contrincante):
    record = 0
    if jugador == contrincante:
        return 'Empate', record
    elif jugador == 'piedra' and contrincante == 'tijera':
        return 'Ganaste', record + 1
    elif jugador == 'papel' and contrincante == 'piedra':
        return 'Ganaste', record + 1
    elif jugador == 'tijera' and contrincante == 'papel':
        return 'Ganaste', record + 1
    else:
        return 'Perdiste', record
    
def main():
    puntaje = 0
    record = 0 
    for i in range(3):
        while True:
            jugador = input('Elige piedra, papel o tijera: ')
            if jugador == 'piedra' or jugador == 'papel' or jugador == 'tijera':
                break
            else:
                print('Opción inválida, intenta de nuevo')

        contrincante = obtener_contrincante()
        print(f'El contrincante eligió: {contrincante}')
        resultado, record = obtener_ganador(jugador, contrincante) # los valores de retorno se guardan en resultado y record para ser usados en el print
        print(resultado) # el resultado se imprime en pantalla para que el jugador sepa si ganó o perdió
        puntaje += record  # se suma el record al puntaje total del jugador para llevar un control de las victorias del jugador en la partida
    print(f'Tu puntaje final es: {puntaje}')

main()