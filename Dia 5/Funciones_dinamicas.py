"""def chequear_3_cifras(numero):
    return numero in range(100,1000)
suma = 548+ 405
resultado = chequear_3_cifras(suma)
print(resultado)"""

def chequear_3_cifras(lista):
    lista_3cifras = []

    for n in lista:
        if n in range (100,1000):
            lista_3cifras.append(n)
        else:
            pass

    return lista_3cifras


resultado = chequear_3_cifras([555,99,600])
print(resultado)