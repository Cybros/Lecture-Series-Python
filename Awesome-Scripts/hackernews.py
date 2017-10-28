#!/usr/bin/env python

from __future__ import print_function
import requests
from bs4 import BeautifulSoup

# get the front page from hacker news
response = requests.request("GET", "https://news.ycombinator.com/")

# convert the response to soup
soup = BeautifulSoup(response.text, "lxml")

# count the things that get processed
count = 0

# process all of the things! :D
for things in soup("tr", { "class" : "athing" }):
    # get at the rank of each thing
    for rank in things("span", { "class" : "rank" }):
        print( rank.text, end=' ' )

    # get the title of each thing
    for title in things("a", { "class" : "storylink" }):
        print( title.text )
        print( title['href'] )
        print( " " )

    count = count + 1

    if count == 10: break
