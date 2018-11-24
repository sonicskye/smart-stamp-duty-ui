import hashlib
import requests
import time
import datetime
import re


#@param BUFF_SIZE is buffer size to read arbitrary file
BUF_SIZE = 65536 #read stuff in 64KB chunks


#@dev getContent will send a request to the url then provide the result
def getcontent(url):
    req = requests.get(url)
    page = req.content
    return page


#@dev quotedstr adds double quotes on a string s
def quotedstr(s):
    return '"%s"'%s


#@dev singlequotedstr adds single quotes on a string s
def singlequotedstr(s):
    return "'%s'"%s


# @dev getsha1string computes sha1 value from a string
# @param x is the string to compute
# @output sha1 value of x
"""
#compute SHA1 from a string
print (getsha1string('ABCD'))
"""
def getsha1string(x):
    h = hashlib.sha1()
    h.update(x.encode('utf-8'))
    return h.hexdigest()


# @dev getsha1file computes sha1 value from a file by reading it in chunks with the size of BUF_SIZE
# @param filepath is the path to the file
# @output sha1 value of the file
"""
#compute SHA1 from a file, the README.md
filepath = 'README.md'
print (getsha1file(filepath))
"""
def getsha1file(filepath):
    h = hashlib.sha1()
    with open(filepath,'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            h.update(data)
    return h.hexdigest()


# @dev functions related to time
# @dev two values are returned, ts in integer and st in string
# @dev ts is seconds after epoch (1 January 1970)
def gettimestamp():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return ts, st


# @dev getwords lists all the words (numbers included) from text
# @dev result is list
# @dev https://stackoverflow.com/questions/7633274/extracting-words-from-a-string-removing-punctuation-and-returning-a-list-with-s
def getwords(text):
    return re.compile('\w+').findall(text)


##################################### test ################################







