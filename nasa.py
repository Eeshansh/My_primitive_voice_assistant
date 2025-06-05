api_key = 'mpArjPDs2jMNtF05qurVcHwG2YSUwOEr2NdcdjiB'

from PIL import Image

import requests
import os
from Listen import Listen



from Speak import Speak1

def nasanews(Date):
    Speak1("let me check if I get something...")
    
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(api_key)

    Params = {'date': str(Date)}
    r = requests.get(Url,params=Params)
    Data = r.json()
    
   
    Info = Data['explanation']

    Title = Data['title']

    image_Url = Data['hdurl']

    image_r = requests.get(image_Url)
    
    FileName = str(Date) + '.jpg'

    with open(FileName, 'wb') as f:
        f.write(image_r.content)
    
    try:
        Path_1 = "D:\\my_work\\Jarvis\\" + str(FileName)

        Path_2 = "D:\\my_work\\Jarvis\\nasa" + str(FileName)

        os.rename(Path_1, Path_2)

        img = Image.open(Path_2)

        img.show()

    except:
        return Speak1("I think there is some issues with the files...trying to configure the issue.")

    Speak1("Ok, I've got something interesting for you...")

    Speak1(f"It is called: {Title}")
    Speak1("and it says that " + Info)
    Speak1("That is all I have for now.")
query = Listen()

 