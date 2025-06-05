from logging import exception
import playsound
import datetime
import tkinter as tk
from tkinter import simpledialog

from Speak import Speak1, wishMe



def alarm(): 
    
    try:
        Speak1("at what time should I set the alarm?")
        ROOT = tk.Tk()
        
        ROOT.withdraw()
        time = simpledialog.askstring(title="Alarm",
                                    prompt="Enter in [H:M] format:")
        
        time_A = datetime.datetime.now() #this has the date,time in hours mins 

    except exception as e:
        return "Ok...exiting alarm mode."


    time_of_day = time_A.strftime("%p")
    hr = time_A.strftime("%I")
    min = time_A.strftime("%M")
    Hr = hr.lstrip('0')
    Min = min.lstrip('0')
    Now = f"{Hr}:{Min}"
    
    if time>Now:
        Speak1(f"Ok, Alarm is set for {time} {time_of_day}")



   
    while True:
        time_A = datetime.datetime.now() #this has the date,time in hours mins
        time_of_day = time_A.strftime("%p")
        hr = time_A.strftime("%I")
        min = time_A.strftime("%M")
        Hr = hr.lstrip('0')
        Min = min.lstrip('0')
        Now = f"{Hr}:{Min}"
        

        if Now == time:
            playsound.playsound("D:\my_work_Jarvis")
            playsound.playsound("D:\my_work_Jarvis")
 
            Speak1("Alarm Closed...")
            wishMe()
            break
        elif time<Now:
            Speak1(f"sorry, I can't set alarm in the Past")
            break

alarm()