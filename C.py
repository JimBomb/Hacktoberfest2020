import requests
from bs4 import BeautifulSoup
import time
import smtplib

def check_price():
    URL = 'your url here'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    title=soup.find(id='productTitle').get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    converted_price=float(price[2:4])*1000+float(price[5:8])
    print(converted_price)
    print(title.strip())
    if (converted_price<12000.0):
        send_mail()

def send_mail():
    toaddr = 'email id '
    cc = ['email id','email id 2']
    bcc = ['email id']
    fromaddr = 'your email'
    toaddrs = [toaddr] + cc + bcc
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your email id','your token')
    subject="Item name"
    body="your message"
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail(fromaddr, toaddrs,msg)
    print("The email has been sent!")
    server.quit()



while (True):
    check_price()
    time.sleep(86400)

