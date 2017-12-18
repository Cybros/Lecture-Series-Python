#!/usr/bin/python
"""Scrapes xkcd comics and saves their images."""

import io
import sys
import requests
from bs4 import BeautifulSoup
from PIL import Image

def crawler(max_pages):
    """Main function for this script; crawls xkcd.com and fetches the images."""

    page = 1
    next_url = ''
    while page <= max_pages:
        url = 'https://xkcd.com' + next_url
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        next_url = soup.findAll(
            'a',
            {'rel': 'prev', 'accesskey': 'p'}
            )[0].get('href')
        image_source = str(soup.findChild('div', {'id': 'comic'}))
        soup2 = BeautifulSoup(image_source, "lxml")
        image_url = 'https:' + soup2.findAll('img')[0].get('src')
        img = requests.get(image_url)
        image = Image.open(io.BytesIO(img.content))
        image.save(sys.argv[2]+image_url.split('/')[4])
        page += 1

crawler(int(sys.argv[1]))
