import speech_recognition as sr

def Listen():
    r = sr.Recognizer()


    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source,0,5)

    try:
        print("Recognising...")
        query = r.recognize_google(audio,language="en-in")
        print(f"You: {query}")

    except:
        return ""

    query = str(query)
    return query.lower()
