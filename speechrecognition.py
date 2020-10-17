import webbrowser
import speech_recognition as sr
import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/Boton")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

MiMQTT = mqtt.Client()
MiMQTT.on_connect = on_connect
MiMQTT.on_message = on_message

MiMQTT.username_pw_set("red", "clave")
MiMQTT.username_pw_set("token", "token")
MiMQTT.connect("broker.shiftr.io", 1883)
MiMQTT.loop_start()




r = sr.Recognizer()


while True:
    with sr.Microphone() as source:
        print('Hola, soy tu asistente por voz: ')
        audio = r.listen(source)
 
        try:
            text = r.recognize_google(audio)
            print('Has dicho: {}'.format(text))
            print(text)
            if "enciende" in text:
                #webbrowser.open('http://amazon.es')
                MiMQTT.publish("LED", "Encender")
                #time.sleep(1)
            if "apaga" in text:
                #webbrowser.open('http://noticiasfinancieras.info')
                MiMQTT.publish("LED", "Apagar")
                #time.sleep(1)
            if "que tal" in text:
                print("Bien y tu?")
        except:
            print('No te he entendido')