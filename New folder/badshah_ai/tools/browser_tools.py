import webbrowser
from urllib.parse import quote_plus

def open_url(url: str) -> str:
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url
    webbrowser.open(url)
    return f"Opened browser: {url}"

def search_web(query: str) -> str:
    url = "https://www.google.com/search?q=" + quote_plus(query)
    webbrowser.open(url)
    return f"Opened search results for: {query}"
