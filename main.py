
# imports
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import http.client
import urllib.request
import re

def main():
    links = {"xkcd.com"}

    for link in links:
        conn = http.client.HTTPSConnection(link)
        conn.request("GET", "/")
        doc = conn.getresponse()
        soup = BeautifulSoup(doc, "html.parser")
        imge = soup.select_one("#comic > img")
        
        src_string = imge['src']

        extension = ".png"
        local_name = link + extension

        urllib.request.urlretrieve("https:" + src_string, local_name)

        #print(src_string)
        #print(soup.prettify())

# run main
main()