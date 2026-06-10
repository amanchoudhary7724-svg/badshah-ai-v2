import webbrowser, requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def open_url(url):
    if not url.startswith(("http://","https://")):
        url = "https://" + url
    webbrowser.open(url)
    return "Opened: " + url

def search_web(q):
    url = "https://www.google.com/search?q=" + quote_plus(q)
    webbrowser.open(url)
    return "Searched: " + q

def scrape(url):
    if not url.startswith(("http://","https://")):
        url = "https://" + url
    html = requests.get(url, timeout=15).text
    return BeautifulSoup(html,"html.parser").get_text("\n", strip=True)[:5000]
