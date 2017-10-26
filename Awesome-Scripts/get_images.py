"""This script loads all images of a website."""

import mimetypes
import requests
from bs4 import BeautifulSoup

while True:
    try:
        url = input("Your Website:")
        website = requests.get(url)
        break
    except:
        print("I can't open the website!")
html = BeautifulSoup(website.text, "html.parser")
images = html.find_all("img")

def download(url, filename):
    file_url = requests.get(url)
    file_extension = mimetypes.guess_extension(file_url.headers['content-type'])
    with open(filename+file_extension, 'wb') as file:
        file.write(file_url.content)

for index, image in enumerate(images):
    download(image["src"], "image{index}".format(index=index))
