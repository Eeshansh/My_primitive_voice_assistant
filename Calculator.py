import wolframalpha
from Speak import Speak1


def WolfRamAlpha(query):
    apikey = "5EKQQH-KHR92KGWQY"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        Speak1("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("jarvis","")
    Term = Term.replace("multiply","*")
    Term = Term.replace("into","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("Add","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")
    Term = Term.replace("by","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        Speak1(f"The Answer is : {result}")

    except:
        Speak1("The value is not answerable")