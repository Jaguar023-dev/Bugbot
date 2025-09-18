import axios
import cheerio
import requests
from bs4 import BeautifulSoup
import os
from random import randint
import re
from PIL import Image
from io import BytesIO
import urllib.request
import time
def sleep(ms):
    time.sleep(ms/1000)
def fetch_buffer(url, options=None):
    if options is None:
        options = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        'DNT': 1,
        'Upgrade-Insecure-Request': 1
    }
    options['headers'] = headers
    res = requests.get(url, **options)
    return res.content
def webp_to_mp4(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        'DNT': 1,
        'Upgrade-Insecure-Request': 1
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    img = soup.find('img')['src']
    img = img.replace('webp', 'png')
    urllib.request.urlretrieve(img, 'img.png')
    return 'img.png'
def fetch_url(url, options=None):
    if options is None:
        options = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    options['headers'] = headers
    res = requests.get(url, **options)
    return res.text
def wa_version():
    url = 'https://web.whatsapp.com/check-update?version=1&platform=web'
    res = requests.get(url)
    return res.text
def get_random(ext):
    return f'{randint(0, 10000)}{ext}'
def is_url(url):
    pattern = re.compile(
        r'^(?:http|ftp)s?://'  #