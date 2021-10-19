import speech_recognition as sr
import pyttsx3 as tts
import serial
import time


#Bot was created with portuguese as main language. If you want to change that, you should change the language in function microphone.recognize_google.
#This bot will be a gate from Python to Arduino'Idle. In this case, i let the program to turn on or turn off the Led's light.

def automacao():

    mon = tts.init()
    microphone = sr.Recognizer()
    repetir = False
    loop = True
    identificação = True
    ser = serial.Serial('COM3', 9600)


    while True:

        with sr.Microphone() as source:

            microphone.adjust_for_ambient_noise(source)
            if repetir == False:

                while True:
                    if loop == True:

                        print("Bem vindo mestre, me chamo Sexta-feira, sou a sua assistente virtual, qual seu nome?")
                        mon.say("Bem vindo mestre, me chamo Sexta-feira, sou a sua assistente virtual, qual seu nome?")
                        mon.runAndWait()
                        mon.stop()

                    nome = microphone.listen(source)

                    try:

                        nomeDoMestre = microphone.recognize_google(nome, language='pt-BR')
                        break

                    except Exception:

                        print("Mestre, pode repetir?")
                        mon.say("Mestre, pode repetir?")
                        mon.runAndWait()
                        mon.stop()
                        loop = False

            print("O que deseja?")
            mon.say("O que deseja?")
            mon.runAndWait()
            mon.stop()


            audio = microphone.listen(source)

        try:

            command = microphone.recognize_google(audio, language='pt-BR')

            if command == 'ligar':

                ser.write('l'.encode())
                time.sleep(1)
                print(f"{nomeDoMestre}, seu pedido de {command} foi realizado")
                mon.say(f"{nomeDoMestre}, seu pedido de {command} foi realizado")
                mon.runAndWait()
                mon.stop()


            elif command == 'desligar':

                ser.write('d'.encode())
                time.sleep(1)
                print(f"{nomeDoMestre}, seu pedido de {command} foi realizado")
                mon.say(f"{nomeDoMestre}, seu pedido de {command} foi realizado")
                mon.runAndWait()
                mon.stop()


            elif command == 'sair':

                print(f"{nomeDoMestre}, seu pedido de {command} foi realizado")
                mon.say(f"Até mais, {nomeDoMestre} ... G!3!X!")
                mon.runAndWait()
                mon.stop()
                break

            repetir = True
        except Exception:

            print("Não entendi")
            mon.say("Não entendi")
            mon.runAndWait()
            mon.stop()
            repetir = True


automacao()