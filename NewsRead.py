import webbrowser
import requests
import json
import pyttsx3
from Listen import Listen
from Speak import Speak1



def latestnews():
    api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=30d4d5dc627b4165976ca8ac6eaba199",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=30d4d5dc627b4165976ca8ac6eaba199",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=30d4d5dc627b4165976ca8ac6eaba199",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=30d4d5dc627b4165976ca8ac6eaba199",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=30d4d5dc627b4165976ca8ac6eaba199",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=30d4d5dc627b4165976ca8ac6eaba199"
}

    content = None
    url = None
    Speak1("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = Listen()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    Speak1("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        Speak1(article)
        news_url = articles["url"]
        #print(f"for more info visit: {news_url}")
        webbrowser.open(news_url)

        query = Listen()
        if "next" in query:
            pass
        elif "stop" in query:
            break
        
    Speak1("ok Sure...")

