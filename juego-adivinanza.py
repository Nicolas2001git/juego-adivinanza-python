import random

numero_secreto = random.randint(0,100)
cant_intentos = 0
cant_max_intentos= 5
adivinado = False
print("Bienvenido al juego de adivinar el numero secreto")

while not adivinado and cant_intentos < cant_max_intentos:
    entrada = int(input("Introduce un numero del 1 al 99: "))
    numero= int(entrada)

    if numero == numero_secreto:
        print("Felicitaciones acertaste")
        adivinado= True
    elif numero < numero_secreto:
        print("El numero es mayor al ingresado")
    else:
        print("El numero es menor al ingresado")
    cant_intentos += 1

if not cant_intentos < cant_max_intentos:
    print("Game over, perdiste pa")