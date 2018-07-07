import requests
import csv
import time
from random import randint
from bs4 import BeautifulSoup
string = raw_input("Enter the Product Name ")
url="http://www.amazon.in/s/keywords="+string
r=requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
link = soup.find("li",{"id":"result_0"})['data-asin']
limit=0
with open(string+'.csv', 'a') as csvfile:
    fieldnames = ['Author', 'date', 'Rating', 'title', 'review']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1,200):
        rurl="http://www.amazon.in/product-reviews/"+link+"/ref=cm_cr_arp_d_paging_btm_2?pageNumber="+str(i)
        r = requests.get(rurl)
        soup = BeautifulSoup(r.content, "lxml")
        review = soup.find_all("div",{"class": "review"})
        print "scrapping page = " + str(i)
        if review == []:
            delay = randint(0,5)
            print "delay ="+str(delay)
            i=i-1
            limit=limit+1
            time.sleep(delay)
            if(limit == 5):
                print "NO MORE REVIEWS"
                break
        else :
            for item in review:
                limit = 0
                author= item.find("a", {"class": "author"}).text
                rate = item.find("span", {"class": "a-icon-alt"}).text
                title = item.find("a", {"class": "review-title"}).text
                date = item.find("span",{"class":"review-date"}).text
                text = item.find("span", {"class": "review-text"}).text
                #print rate+" /////  "+title+"///"+date+"////"+text+"\n"
                try:
                    writer.writerow(
                        {'Author': author,
                         'date': date ,
                         'Rating': rate,
                         'title': title,
                         'review': text})
                except Exception:
                    pass