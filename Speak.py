import datetime
import pyttsx3
def Speak1(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',180)
    print(f"Jarvis : {Text}")
#    print(voices)
    engine.say(Text)
    engine.runAndWait()


def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            Speak1("Good Morning!")

        elif hour>=12 and hour<16:
            Speak1("Good Afternoon!")   

        else:
            Speak1("Good Evening!") 

#Speak1("hello friends!")