#args= se refiere a argumentos, nos permiten definir funciones cuyo numero de argumentos sea variable (funciones genericas que se adaptan al numero de argumentos que el usuario quiera pasar)

def suma(*args):
    total = 0

    for arg in args:
        total += arg

    return total

print(suma(5,6,8))
