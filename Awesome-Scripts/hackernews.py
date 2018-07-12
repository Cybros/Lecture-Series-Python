#!/usr/bin/env python

from __future__ import print_function
import argparse
import requests
from bs4 import BeautifulSoup

# check to see if a number was passed in
parser = argparse.ArgumentParser()
parser.add_argument(
    'news_count', metavar='int', type=int, choices=range(1,31), 
    nargs='?', default=10, 
    help='Then number of news items to return, from 1 to 30')

args = parser.parse_args()

# get the front page from hacker news
response = requests.request("GET", "https://news.ycombinator.com/")

# convert the response to soup
soup = BeautifulSoup(response.text, "lxml")

# process all of the things! :D
for things in soup("tr", { "class" : "athing" })[:args.news_count]:
    # get at the rank of each thing
    for rank in things("span", { "class" : "rank" }):
        print( rank.text, end=' ' )

    # get the title of each thing
    for title in things("a", { "class" : "storylink" }):
        print( title.text )
        print( title['href'] )
        print( " " )
