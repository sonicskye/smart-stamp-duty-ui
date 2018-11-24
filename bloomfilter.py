'''
sonicskye
bloomfilter.py

Requirements:
bitarray (https://github.com/ilanschnell/bitarray)
pybloof (https://github.com/jhgg/pybloof)
'''

import pybloof
import utilities as u


def createstringbloomfilter(wordlist):
    # if the size is too small then the result is inaccurate
    # makes sure that there is an extra 500 allowance
    sz = len(wordlist) + 500
    bf = pybloof.StringBloomFilter(size=sz, hashes=9)
    for word in wordlist:
        #bf.add(word)
        if word not in bf:
            bf.add(word)
    return bf.to_base64().decode('utf-8')


def teststringbloomfilter(bfValue, wordlist):
    bf = pybloof.StringBloomFilter.from_base64(bfValue.encode('utf-8'))
    wlength = len(wordlist)
    positive = 0
    for word in wordlist:
        if word in bf:
            positive += 1;
    res = round(positive/wlength *100)
    return res


##################################### test ################################


