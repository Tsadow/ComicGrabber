# a script to collect webcomics for easier reading that individually visiting sites

# imports
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import http.client
import urllib.request
import re

# "statics"
_extension = ".png"

# main funcion
def main():
    get_xkcd()
    #get_dhs()
    get_mollybeans()
    get_callmechuck()
    get_gwtb()

# non-comic-specific

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

def get_src_string(soup, path_to_img):
    # follow given document tree path to img element
    img = soup.select_one(path_to_img)
    # return src attribute of img element
    return img['src']

# comic-specific

def get_xkcd():
    link = "xkcd.com"
    # https  
    soup = get_document_object_https(link)

    # get the src
    path_to_img = "#comic > img"   
    src_string = get_src_string(soup, path_to_img)

    # build filename string
    local_name = link + _extension

    # download the comic (includes a fix for how the site references the image files)
    urllib.request.urlretrieve("https:" + src_string, local_name)

def get_dhs():
    link = "donthitsave.com"
    # https  
    soup = get_document_object_https(link)

    # get the src
    path_to_img = ".comicfull"
    src_string = get_src_string(soup, path_to_img)

    # build filename string
    local_name = link + _extension

    # download the comic !!!doesn't work yet due to ssl/sni issue
    urllib.request.urlretrieve(src_string, local_name)

def get_mollybeans():
    link = "mollybeans.com"
    # https  
    soup = get_document_object_https(link)

    # get the src
    path_to_img = ".entry-comic > article > a > img"
    src_string = get_src_string(soup, path_to_img)

    # build filename string
    local_name = link + _extension

    # download the comic
    urllib.request.urlretrieve(src_string, local_name)

def get_callmechuck():
    link = "callmechuckcomic.com"
    # http  
    soup = get_document_object_http(link)

    # get the src
    path_to_img = ".entry-comic > article > a > img"
    src_string = get_src_string(soup, path_to_img)

    # build filename string
    local_name = link + _extension

    # download the comic
    urllib.request.urlretrieve(src_string, local_name)

def get_gwtb():
    link = "www.blastwave-comic.com"
    # http  
    soup = get_document_object_http(link)

    # get the src
    path_to_img = ".comic_title ~ img"
    src_string = get_src_string(soup, path_to_img)

    #nonstandard src_string because of how site references the image files
    src_string = "http://www.blastwave-comic.com" + src_string[1:]

    # build filename string
    local_name = link + _extension

    # download the comic
    urllib.request.urlretrieve(src_string, local_name)

# run main
main()