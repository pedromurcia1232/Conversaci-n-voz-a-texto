from cgitb import text
import pyttsx3
import speech_recognition as sr


enige=pyttsx3.init()
r= sr.Recognizer()
engine=pyttsx3.init()
engine.setProperty("rate",150)


while (True):
    with sr.Microphone() as source:
    
     print("Comienza hablar...")
     habla="Comienza hablar"
     engine.say(habla)
     engine.runAndWait()
        
     audio = r.listen(source)
    

     try:
         text = r.recognize_google(audio, language='es-Es')
         print(": {}".format(text))
         x1=(input("Respuesta: "))
         print(x1)
         engine.say(x1)
         engine.runAndWait()
        
        
        
     except:
         print("Lo sentimos¡ no se pudo entender lo que dijo")
         perdon="Lo sentimos¡ no se pudo entender lo que dijo"
         engine.say(perdon)
         engine.runAndWait()
        