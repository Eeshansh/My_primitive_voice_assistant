import time
from Speak import Speak1



def time_with_seconds():
    time1 = time.localtime()
    current_time = time.strftime("%H:%M", time1)
    current_time1 = int(time.strftime("%H",time1))
    current_time2 = time.strftime("%M" , time1)
    
    if current_time1>=0 and current_time1<12:
        Speak1(f"It is {current_time}"+" AM ")

    elif current_time1==12:
        Speak1(f"It is {current_time}"+" PM ")
    else:
        currenttime = (current_time1) - (12)
        Speak1(f"It is {currenttime}:{current_time2}"+" PM ")

