import pywhatkit
from Speak import Speak1
from Listen import Listen

def music():
        Speak1("Tell Me The Name of The Song!")
        musicName = Listen()            
        
        pywhatkit.playonyt(musicName)
        
        Speak1("Your Song has Started! I hope you will like it!")
