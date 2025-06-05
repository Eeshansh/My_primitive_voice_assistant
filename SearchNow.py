import wikipedia
import pywhatkit
import webbrowser
from Speak import Speak1






def searchGoogle(query):
    Speak1("Here's what I found......")
    try:
            reply = pywhatkit.search(query)

            Speak1(reply)

            Speak1("and these are the best possible results")

    except:
            Speak1("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        Speak1("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        Speak1("Done Sir")

def searchWikipedia(query):
    if "who" in query or "where" in query or "what" in query or "why" in query or "when" in query or "how" in query or "whom" in query or "whose" in query:
        Speak1("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        Speak1("According to wikipedia..")
        print(results)
        Speak1(results)
