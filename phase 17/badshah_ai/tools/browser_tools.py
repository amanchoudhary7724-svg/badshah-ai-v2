import webbrowser
from urllib.parse import quote_plus
def open_url(url):
    if not url.startswith(("http://","https://")):
        url = "https://" + url
    webbrowser.open(url); return "Opened: " + url
def search_web(query):
    url = "https://www.google.com/search?q=" + quote_plus(query)
    webbrowser.open(url); return "Searched: " + query
