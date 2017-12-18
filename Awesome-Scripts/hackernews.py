#!/usr/bin/env python
"""Script to scrape Hackernews and retrieve top 10 links."""

from __future__ import print_function
import requests
from bs4 import BeautifulSoup

# Get the front page from hacker news.
response = requests.request("GET", "https://news.ycombinator.com/")
# Convert the response to soup.
soup = BeautifulSoup(response.text, "lxml")
# Count the things that get processed.
count = 0

# Process all of the things! :D
for things in soup("tr", {"class": "athing"}):
    # Get at the rank of each thing.
    for rank in things("span", {"class": "rank"}):
        print(rank.text, end=' ')

    # Get the title of each thing.
    for title in things("a", {"class": "storylink"}):
        print(title.text)
        print(title['href'])
        print()

    count += 1

    if count == 10:
        break
