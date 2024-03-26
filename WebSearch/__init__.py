#program:       __init__
#purpose:       
#progamer:      Themadhood Pequot 11/22/2023

_FILE = "WebSearch.__init__"
_VERSION = "0.0.1"

import Error
from googlesearch import search
from bs4 import BeautifulSoup
import requests

io = Error.io

"""
try:
    pass

except Exception as e:
    if self._Error:
        raise
    Error.UploadError([_FILE,_VERSION,"class","def",
                                f"mesage",e],"Functions")"""


def Search(query,Max=5):
    st = Error.time.time()
    Error.Log(f"starting search for: {query}","Log.txt")
    resalts = []
    for resalt in search(query, tld="co.in", num=Max, stop=Max, pause=2):
        resalts.append(resalt)

    Error.Log(f"search runtime: {Error.LenTime(st)} {Max} resalts found",
              "Log.txt")
    return resalts

def ReadPage(url):
    Error.Log(f"Reading wepage: {url}","Log.txt")
    #get URL data
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    res.close()
    #get body
    text = soup.body.text
    text = RemoveLineswithSpases(text)
    text = RemoveUnesisarySpace(text)

    #return title, content, url
    return soup.title.text,text,url

def RemoveUnesisarySpace(text):
    if "\n\n\n" in text:
        text = RemoveUnesisarySpace(text.replace("\n\n\n","\n\n"))
    return text

def RemoveLineswithSpases(text):
    remove = []
    textSplit = text.split("\n")
    for line in textSplit:
        if line.isspace() and line not in remove:
            remove.append(line)

    while remove > []:
        text = text.replace(f"{remove.pop()}\n","\n")

    return text



if __name__ == "__main__":
    resalts = Search("meaning hi")

    txt = ReadPage(resalts[0])
    print(txt[2],"\n\n",txt[0],"\n\n",txt[1])





