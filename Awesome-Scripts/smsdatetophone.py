from datetime import datetime
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler
from twilio.rest import Client



account_sid = "AC1f976a88c613ec4405f2d96155f9e505"
auth_token = "yourtoken"
def some_job():
    quote_page = 'https://www.timeanddate.com/'

    page = urllib.request.urlopen(quote_page)


    soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of time and get its value
    name_box = soup.find('span', attrs={'id': 'clk_hm'})

    name = name_box.text # strip() is used to remove starting and trailing

    
    client = Client(account_sid, auth_token)

    client.messages.create(
     to="+919575441312", 
     from_="(201) 430-7057",
     body=name,
     media_url="https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg")
    

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds=10)
scheduler.start()
