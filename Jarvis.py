import datetime
import tkinter as tk
from tkinter import simpledialog
import os
import tkinter
import webbrowser
from ast import While
from Listen import Listen

from tkinter import Button, Entry, Label, StringVar, Tk


#import playsound
import pyautogui
import pyjokes

import requests
from bs4 import BeautifulSoup
from pytube import YouTube



from Speak import Speak1, wishMe
from Take_Screenshot import screenshot
#from Clap import Tester


if __name__ == "__main__":
    # playsound.playsound("D:\\my_work\\Jarvis\\beep_sound.mp3")
    #Tester()
    from Speak import wishMe
    wishMe()

    while True:
        query = Listen() #hearing and command accepting 2

        if 'what' in query or 'why' in query or 'when' in query or 'whom' in query or 'whose' in query or 'how' in query or 'tell me' in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
       

        elif 'i am back' in query:
            Speak1("Welcome back...Sir")
        
        
        
        elif 'take a break' in query:
            Speak1("Ok Sir, I will be Available when you need me.")
            Speak1("Just Say Wake Up Jarvis!")
            

        elif 'wake up'in query:
            Speak1("I'm all ears...please tell me.")
        
        
        elif 'who are you' in query or ' yourself' in query:
            Speak1("Allow me to introduce myself, I am Jarvis. A Virtual Artificial Intelligence. And I am here to Assist you with a variety of tasks as best I can, 24 hours a day, 7 days a week...Systems are now fully Operational and I'm ready.")



        elif 'can you hear' in query or 'are you listening' in query:
            Speak1("Yes Sir I can hear you loud and clear...")    
                
            

        elif 'screenshot' in query:
            screenshot()

        

        elif 'time' in query:
            pass
            from Clock import time_with_seconds
            time_with_seconds()
            

        elif 'date' in query:
            from datetime import date
            strdate = datetime.datetime.now().strftime("%Y/%m/%d")
            Speak1(f"Today's Date is: {strdate}")

        elif 'day' in query:
            from current_day import tellDay
            tellDay()

        elif 'turn off' in query:
            Speak1("Ok Sir, All Systems are being shutdown and your Computer will be on manual mode....")
            from sys import exit
            exit()
                
        elif 'music' in query or 'gana baja' in query or 'song' in query:
            import Music 
            Music.music()

        

        elif 'joke' in query:
                
            get = pyjokes.get_joke()
            Speak1(get)

        elif 'repeat after me' in query:
            Speak1("Please Speak I will follow...")
            While('repeat'in query) 

            jj = Listen()
            Speak1(f"You Said : {jj}")

        

        elif "pause" in query:
            pyautogui.press("k")
            Speak1("video paused")
        elif "play" in query:
                pyautogui.press("k")
                Speak1("video played")
        elif "mute" in query:
                pyautogui.press("m")
                Speak1("video muted")
        elif "switch the tab" in query:
                pyautogui.hotkey("alt","tab")
                Speak1("there you go")

        elif "unmute the video" in query:
                pyautogui.press("m")
                Speak1("video muted")
        
        elif "full screen" in query:
                pyautogui.press("f")
                Speak1("Okay")
                query = Listen()
                if "exit" in query:
                    pyautogui.press("esc")
                    Speak1("Ok")
        
        elif "back" in query:
            pyautogui.press('left') 

        elif "back 10 second" in query:
            pyautogui.press('j')

        elif "forward 10 second" in query:
            pyautogui.press('L')  

        elif "foward" in query:
            pyautogui.press('Right')

        elif "new tab" in query:
            pyautogui.hotkey("ctrl","t")
            Speak1("New tab Opened")

        elif "close the tab" in query:
            pyautogui.hotkey("ctrl","w")
            Speak1("tab Closed")

        elif "minimise window" in query:
            pyautogui.hotkey("win","down")
            Speak1("window minimized")
            
        elif "maximise window" in query: 
            pyautogui.hotkey("win","up")
            Speak1("window maximised")

        elif "downloads" in query:
            pyautogui.hotkey("ctrl","j")
            Speak1("here's browser downloads section....")

        elif "print" in query:
            pyautogui.hotkey("ctrl","p")
            Speak1("Please take the hard copy of the data.")

            
        elif "show recent tabs" in query:
            pyautogui.hotkey("windows","shift","t")
            Speak1("here's the recent tabs")


        elif "Refresh window" in query or "reload window" in query or "refresh tab" in query or "reload tab" in query:
            pyautogui.hotkey("ctrl","r")
            Speak1("Alright.....")

        elif "history" in query:
            pyautogui.hotkey("ctrl","h")

        elif "switch tab" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            while True:
                    kk = Listen()
                    while 'next' in kk:
                            pyautogui.press("tab")
                            kk = Listen()
                            if 'yes' in kk:
                                    pyautogui.keyUp('alt')
                                    break
                    break


        elif "save tab" in query:
            pyautogui.hotkey("ctrl","d")


            
        elif "volume up" in query:
                from keyboard import volumeup
                Speak1("Turning volume up,sir")
                volumeup()

    
        elif "volume down" in query:
                from keyboard import volumedown
                Speak1("Turning volume down, sir")
                volumedown()


        elif "launch" in query:  #only for opening websites.
                #query = query.replace("launch"," ")
                query = query.replace("dot",".")
                from Dictapp import openappweb
                openappweb(query)
        elif "close tab" in query: #only for closing tabs.
                from Dictapp import closeappweb
                closeappweb(query)

            
            
        elif "google" in query:
                from SearchNow import searchGoogle
                searchGoogle(query)
        elif "youtube" in query:
                from SearchNow import searchYoutube
                searchYoutube(query)
        elif "wikipedia" in query:
                from SearchNow import searchWikipedia
                searchWikipedia(query)


            
            
        elif "remember that" in query:
                rememberMessage = query.replace("remember that"," ")
                rememberMessage = query.replace("jarvis"," ")
                Speak1(rememberMessage)
                remember = open("Remember.txt","a")
                remember.write(rememberMessage)
                remember.close()
        
        elif "you remember" in query or "is there something I need to know" in query:
                if os.path.getsize('E:\\Jarvis\\Remember.txt') != 0:
                    remember = open("Remember.txt","r")
                    query = query.replace("remember that"," ")
                    Speak1("Yes, you said that: " + remember.read())
                elif os.path.getsize('E:\\Jarvis\\Remember.txt') == 0:
                    Speak1("Oh...I don't remeber you telling me to remember anything...")
        
        
        elif "news" in query:
                from NewsRead import latestnews
                latestnews()

        elif "calculate" in query or "calculator" in query:
                from Calculator import Calc,WolfRamAlpha
                query = query.replace("calculate","")
                query = query.replace("jarvis","")
                Calc(query)

        
                

        elif 'video downloader' in query:
                root = Tk()
                root.geometry('500x300')
                root.resizable(0,0)
                root.title("Youtube Video Downloader")
                Speak1("Enter Video Url Here !")
                Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
                link = StringVar()
                Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
                Entry(root,width = 70,textvariable = link).place(x=32,y=90)

                def VideoDownloader():
                    url = YouTube(str(link.get()))
                    video = url.streams.first()
                    video.download()
                    Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

                Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

                root.mainloop()
                Speak1("Video Downloaded")
                
        elif 'temperature' in query:
                search = "temperature in Bangalore"
    
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temperature = data.find("div", class_ = "BNeawe").text
                Speak1(f"The Temperature Outside Is {temperature}")

                Speak1("Do you want me to give temperature of some other place?")
                next = Listen()
                while('yes' in next):
                    Speak1("okay...Tell me the Name Of the Place? ")
                    name = Listen()
                    search = f"temperature in {name}"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temperature = data.find("div",class_ = "BNeawe").text
                    Speak1(f"The Temperature in {name} is {temperature}")

                    Speak1("Do you want me to give to temperature of some other place?")
                    next = Listen()
    
                    if 'no' in next:
                        Speak1('what else can I do for you?') 
        
                    else:
                        Speak1("no problem sir")

        elif 'close it' in query: #any desktop app
            pyautogui.hotkey("alt","f4")
            Speak1("Done!")

        

        elif "shutdown the system" in query:
                Speak1("Are You sure you want to shutdown")
                shutdown = Listen()
                if shutdown == "yes":
                    os.system("shutdown /s /t 0")
                                    
                elif shutdown == "no":
                    break

                                
        elif "cricket score" in query:
            Speak1("Sure...Getting latest updates for cricket")
            import requests  # pip install requests
            from bs4 import BeautifulSoup  # pip install bs4
            from plyer import notification  # pip install plyer
            url = "https://www.cricbuzz.com/"
            page = requests.get(url)
            soup = BeautifulSoup(page.text,"html.parser")
            team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
            team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
            team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
            team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

            a = print(f"{team1} : {team1_score}")
            
            b = print(f"{team2} : {team2_score}")

            tkinter.messagebox.showinfo(
                    title = "CRICKET SCORE :- ",
                    message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                )

        
        elif 'play a game' in query:
            from game import game_play
            game_play()

        elif 'my business website' in query or 'business site' in query:
                Speak1("Lauching Sai Glass Business Website...")
                webbrowser.open(f"https://saiglassworld.xyz/")

        elif 'alarm' in query:
            
            from alarm import alarm
            alarm()

        elif 'space data' in query:
            Speak1("Ok, Give me the date first...")
            Speak1("I can access data from 16th June 1995 till date only...I'm sorry i don't have any data with me prior to that date.")
            ROOT = tk.Tk()

            ROOT.withdraw()
            USER_INP = simpledialog.askstring(title="Space News",
                                                prompt="Enter your desired Date[Y:M:D]: ")
            date = USER_INP
            from nasa import nasanews
            nasanews(date)    
       