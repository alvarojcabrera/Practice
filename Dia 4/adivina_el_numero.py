from random import randint
estimado = 0
intentos = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")
print(f" Bueno {nombre}, he pensado un número entre 1 y 100\n Tienes 8 intentos para advinarlo")

while intentos < 8:
    estimado = int(input("Cuál es el numero?: "))
    intentos += 1
    if estimado not in range(1,101):
        print("Tu número no se encuentra en el rango de 1 a 100")
    elif estimado < numero_secreto:
        print("El número es más alto")
    elif estimado > numero_secreto:
        print("El número es más bajo")
    else:
        print(f"Felicidades {nombre}! Has adivinado en {intentos} intentos!")
        break


if estimado != numero_secreto:
    print(f"Lo lamento, se agotaron los intentos, el numero secreto era {numero_secreto}!")




