# a script to collect webcomics for easier reading that individually visiting sites

# imports
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import http.client
import urllib.request
import re

def main():
    get_xkcd()
    #get_dhs()
    get_mollybeans()
    get_callmechuck()
    get_gwtb()

def get_document_object_https(link):
    conn = http.client.HTTPSConnection(link)
    conn.request("GET", "/")
    doc = conn.getresponse()
    return BeautifulSoup(doc, "html.parser")

def get_document_object_http(link):
    conn = http.client.HTTPConnection(link)
    conn.request("GET", "/")
    doc = conn.getresponse()
    return BeautifulSoup(doc, "html.parser")

def get_xkcd():
    link = "xkcd.com"
    soup = get_document_object_https(link)

    imge = soup.select_one("#comic > img")    
    src_string = imge['src']

    extension = ".png"
    local_name = link + extension

    urllib.request.urlretrieve("https:" + src_string, local_name)

def get_dhs():
    link = "donthitsave.com"
    soup = get_document_object_https(link)

    imge = soup.select_one(".comicfull")
    src_string = imge['src']

    extension = ".png"
    local_name = link + extension

    urllib.request.urlretrieve(src_string, local_name)

def get_mollybeans():
    link = "mollybeans.com"
    soup = get_document_object_https(link)

    imge = soup.select_one(".entry-comic > article > a > img")
    src_string = imge['src']

    extension = ".png"
    local_name = link + extension

    urllib.request.urlretrieve(src_string, local_name)

def get_callmechuck():
    link = "callmechuckcomic.com"
    soup = get_document_object_http(link)

    imge = soup.select_one(".entry-comic > article > a > img")
    src_string = imge['src']

    extension = ".png"
    local_name = link + extension

    urllib.request.urlretrieve(src_string, local_name)

def get_gwtb():
    link = "www.blastwave-comic.com"
    soup = get_document_object_http(link)

    imge = soup.select_one(".comic_title ~ img")
    src_string = imge['src']

    #nonstandard src_string because of how site references the image files
    src_string = "http://www.blastwave-comic.com" + src_string[1:]

    extension = ".png"
    local_name = link + extension

    urllib.request.urlretrieve(src_string, local_name)

# run main
main()