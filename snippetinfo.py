import requests,pywhatkit
from Speak import Speak1
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import wikipedia

def snipinfo():
    chrome_options = Options()
    chrome_options.add_argument('--log-level=3')
    chrome_options.headless = True
    user_query = input('Enter your query: ')
    #pywhatkit.search(user_query)
    result = wikipedia.summary(user_query,2)
    Speak1(result)

