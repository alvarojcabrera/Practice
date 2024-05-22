kills= input("Dime cuantas kills tienes: ")
Assist= input("Dime cuantas asistencias tienes: ")
Deaths= input("Dime cuantas veces has muerto: ")

kills =int(kills)
Assist=int(Assist)
Deaths=int(Deaths)

kda= (kills + Assist)/Deaths

print(f" Felicidades, tu KDA es {kda}")