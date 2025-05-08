import requests
from bs4 import BeautifulSoup

def crawl_static_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.prettify()
