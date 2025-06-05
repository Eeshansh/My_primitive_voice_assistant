import pyautogui
from Speak import Speak1
from time import sleep







def closeappweb(query):
    Speak1("Closing,sir")
    if "one tab" in query or "1 tab" in query or "this tab" in query or "the tab" in query:
        pyautogui.hotkey("ctrl","w")
        Speak1("All tabs closed")
    elif "2 tab" in query or 'both tab' in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        Speak1("All tabs closed")
    elif "three tab" in query or '3 tab' in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        Speak1("All tabs closed")
        
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        Speak1("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        Speak1("All tabs closed")

    


