import pyttsx3
import speech_recognition as sr
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro microfono y devolver audio como texto

def transformar_audio_en_texto():
    # almacenar
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzó a grabar
        print("ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google(audio, language="es-col")

            # Preba de que si entró
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido
        # en caso de no entender

        except sr.UnknownValueError:
            # prueba de que no entró
            print("Ups, no entendí")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:
            # prueba de que no entró
            print("Ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variabel para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # dias
    calendario = {0: "Lunes",
                  1: "Martes",
                  2: "Miércoles",
                  3: "Jueves",
                  4: "Viernes",
                  5: "Sábado",
                  6: "Domingo"}

    # decir el dia de la semana
    hablar(f"Hoy es: {calendario[dia_semana]}")


# informar que hora es
def pedir_hora():

    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} y {hora.second} segundos"
    print(hora)

    # decir hora
    hablar(hora)


# Saludo inicial
def saludo_inicial():

    # Variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"

    # decir el saludo
    hablar(f"{momento}, soy Alba, tu asistente personal. Cuéntame, ¿En que te puedo ayudar?")


# FUNCION CENTRAL DEL ASISTENTE!!!!!!
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True

    # Loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando eso en Wikipedia")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Wikipedia dice lo siguiente")
            hablar(resultado)
            continue
        elif "busca en internet" in pedido:
            hablar("Ya mismo estoy en eso")
            pedido = pedido.replace("busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            buscar = pedido.replace("reproducir", "").strip()
            hablar("Que temazo, buscando en YouTube")
            webbrowser.open(f"https://www.youtube.com/results?search_query={buscar}")
            continue
        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue

        elif "adiós" in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas")
            break


pedir_cosas()








