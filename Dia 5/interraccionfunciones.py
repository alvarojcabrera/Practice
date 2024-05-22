from random import shuffle

#CREAR LISTA

palitos = ["-","--", "---", "----"]

#Mezclar palitos

def mezclar(lista):
    shuffle(palitos)
    return  lista

# Pedirle intento
def probar_suerte():
    intento = ""
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un numero del 1 al 4: ")
    return int(intento)

# Comprobar intento
def chequear_intento(lista,intento):
    if lista[intento - 1] == "-":
        print("Perdiste pa")
    elif lista[intento - 1 ] == "--":
        print("Pego en el palo rey")
    else:
        print("No te tocó")

    print(f"Te ha tocado {lista[intento-1]}")


palitos_mezclados = mezclar(palitos)
seleccion=probar_suerte()
chequear_intento(palitos_mezclados,seleccion)
