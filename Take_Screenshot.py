from Speak import Speak1
from Listen import Listen
import pyautogui
import os

def screenshot():
        Speak1("Ok sure, What Should I Name That File ?")
        path = Listen()
        path1name = path + ".jpg"
        path1 = "C:\\Users\\SMRITI\\Pictures\\screenshots"+ path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\SMRITI\\Pictures\\")


        
        Speak1("Here Is Your ScreenShot") 


