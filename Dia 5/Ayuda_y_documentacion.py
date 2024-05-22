def saludar_persona(nombre):
    print("Hola " + nombre)

saludar_persona("Fernando")
saludar_persona("Javier")

#Respecto a Return

def multiplicar(numero1,numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(5,10)
print(resultado)
