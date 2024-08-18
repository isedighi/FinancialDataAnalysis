# copied from urllinks.py


import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import ssl
import re
import html
import time

'''
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
'''


def call_stock(stock):
    headers = {
        "Cache-Control": "no-cache",
        "Expires": "0"
    }
    url = stock
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    extract_all = soup.find_all(name='span')
    extracted = extract_all[60]
    price = extracted.contents

    #price = extract
    extract_all = soup.find_all(name='h1')
    extracted = extract_all[1]
    symbol = extracted.contents

    #symbol = extract
    if len(price) < 1:
        price.append('n/a')
    print("\n", symbol[0], 'price:', price[0], '\n')

    response.close()
