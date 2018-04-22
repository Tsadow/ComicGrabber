
# imports
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import http.client

def main():
    links = {"xkcd.com"}

    for link in links:
        conn = http.client.HTTPSConnection(link)
        conn.request("GET", "/")
        doc = conn.getresponse()
        soup = BeautifulSoup(doc, "html.parser")
        print(soup.prettify())

# run main
main()