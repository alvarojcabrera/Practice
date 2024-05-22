mi_variable = "hola mundo"
#Pero Boleano seria, este diria "falso"
mi_bool = 10 == 25

#Respecto a los operadores logicos...
boole_ = 4 < 5 and 5 > 6
print(boole_)

# if num1 > num2:
  #  print(f"{num1} es mayor que {num2}")
#elif num2 > num1:
 #   print(f"{num2} es mayor que {num1}")
# else:
 #   print(f"{num1} y {num2} son iguales")


lista = ["a","b","c"]

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f" Letra {numero_letra}: {letra}")

from random import *

aleatorio= choice(lista)
print(aleatorio)