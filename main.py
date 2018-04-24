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
    # make https connection to given URL
    conn = http.client.HTTPSConnection(link)
    conn.request("GET", "/")
    # get the content of the webpage
    doc = conn.getresponse()
    # return a beautiful soup object made from the webpage content
    return BeautifulSoup(doc, "html.parser")

def get_document_object_http(link):
    # make http connection to given URL
    conn = http.client.HTTPConnection(link)
    conn.request("GET", "/")
    # get the content of the webpage
    doc = conn.getresponse()
    # return a beautiful soup object made from the webpage content
    return BeautifulSoup(doc, "html.parser")

def get_xkcd():
    link = "xkcd.com"
    # https  
    soup = get_document_object_https(link)

    # go to the img element containing the comic and get the src
    imge = soup.select_one("#comic > img")    
    src_string = imge['src']

    # building strings
    extension = ".png"
    local_name = link + extension

    # download the comic (includes a fix for how the site references the image files)
    urllib.request.urlretrieve("https:" + src_string, local_name)

def get_dhs():
    link = "donthitsave.com"
    # https  
    soup = get_document_object_https(link)

    # go to the img element containing the comic and get the src
    imge = soup.select_one(".comicfull")
    src_string = imge['src']

    # building strings
    extension = ".png"
    local_name = link + extension

    # download the comic !!!doesn't work yet due to ssl/sni issue
    urllib.request.urlretrieve(src_string, local_name)

def get_mollybeans():
    link = "mollybeans.com"
    # https  
    soup = get_document_object_https(link)

    # go to the img element containing the comic and get the src
    imge = soup.select_one(".entry-comic > article > a > img")
    src_string = imge['src']

    # string building
    extension = ".png"
    local_name = link + extension

    # download the comic
    urllib.request.urlretrieve(src_string, local_name)

def get_callmechuck():
    link = "callmechuckcomic.com"
    # http  
    soup = get_document_object_http(link)

    # go to the img element containing the comic and get the src
    imge = soup.select_one(".entry-comic > article > a > img")
    src_string = imge['src']

    # string building
    extension = ".png"
    local_name = link + extension

    # download the comic
    urllib.request.urlretrieve(src_string, local_name)

def get_gwtb():
    link = "www.blastwave-comic.com"
    # http  
    soup = get_document_object_http(link)

    imge = soup.select_one(".comic_title ~ img")
    src_string = imge['src']

    #nonstandard src_string because of how site references the image files
    src_string = "http://www.blastwave-comic.com" + src_string[1:]

    # string building
    extension = ".png"
    local_name = link + extension

    # download the comic
    urllib.request.urlretrieve(src_string, local_name)

# run main
main()