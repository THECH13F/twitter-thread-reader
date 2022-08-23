
import requests
from bs4 import BeautifulSoup
import json
tweetid=input("enter tweet id:")
baseurl=f'https://threadreaderapp.com/thread/{tweetid}.html'
try:
    r = requests.get(baseurl)
    soup = BeautifulSoup(r.content, 'html5lib')
except:
    print("!!An error occured!! \nprossible reasons are\n1. problem with your internet\n2. error in stablishing connection\nPLEASE TRY AGAIN AFTER SOMETIME")
quotes=[]
data_html={}
file_html=""
text = soup.find('a', {'class': 'twitter-follow-button'})
def print_html():
    num=0
    for i in range(len(text.text)):
        if text.text[i]=='@':
            username=text.text[i+1:]
    with open(f'{username}_thread_{tweetid}.html', 'w', encoding='utf-8') as f:
        f.write(f'<html><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css" integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog==" crossorigin="anonymous" />\
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha512-c8AIFmn4e0WZnaTOCXTOLzR+uIrTELY9AeIuUq6ODGaO619BjqG2rhiv/y6dIdmM7ba+CpzMRkkztMPXfVBm9g==" crossorigin="anonymous" />\
    <link href="https://fonts.googleapis.com/css?family=Lato|Sanchez:400italic,400|Abhaya+Libre" rel="stylesheet">\
    <link rel="stylesheet" media="all" href="https://threadreaderapp.com/assets/application-9f9069ec8529cb7bafce100a35613e23e8916ee98bd5178fa0ee395ec0a19a84.css" data-turbolinks-track="reload" />\
    <link rel="stylesheet" media="screen" href="https://threadreaderapp.com/assets/components/loading-4d00727d71e1da9d3c71e41fc14ba962c448080ad5f92bb408782958800fc6a7.css" /><body>')
        while(True):
            num+=1
            table = soup.find('div', attrs = {'id':f'tweet_{num}'})
            if str(table) == "None":
                break
            else:
                f.write(str(table))
        f.write('</body></html>')
def print_json():
    num=0
    for i in range(len(text.text)):
        if text.text[i]=='@':
            username=text.text[i+1:]
    while(True):
        num+=1
        table = soup.find('div', attrs = {'id':f'tweet_{num}'})
        if str(table) == "None":
            break
        else:
            html=quotes.append(table.text)
    data_html[username]=quotes
    with open(f'{username}_thread_{tweetid}.json', 'w', encoding='utf-8') as f:
        json.dump(data_html, f, ensure_ascii=False)
def print_text_file():
    num=0
    for i in range(len(text.text)):
        if text.text[i]=='@':
            username=text.text[i+1:]
    with open(f'{username}_thread_{tweetid}.txt', 'w', encoding='utf-8') as f:
        while(True):
            num+=1
            table = soup.find('div', attrs = {'id':f'tweet_{num}'})
            if str(table) == "None":
                break
            else:
                f.write(table.text)
print("Which format you need \n1. JSON \n2. TXT file\n3. HTML file\n4. ALL format")
choice=input("choose one of them:")
if choice=='1':
    try:
        print_json()
    except:
        print("Thread can be inaccessible because:\nThe thread is too old (we can only retrieve 3200 tweets per user)\nThe thread was deleted on Twitter by the author or by Twitter\nThe Twitter account was deleted by the author or by Twitter\nThe Twitter account was banned/suspended by Twitter\nThe author blocked us on Twitter or it's a private account")
elif choice=='2':
    try:
        print_text_file()
    except:
        print("Thread can be inaccessible because:\nThe thread is too old (we can only retrieve 3200 tweets per user)\nThe thread was deleted on Twitter by the author or by Twitter\nThe Twitter account was deleted by the author or by Twitter\nThe Twitter account was banned/suspended by Twitter\nThe author blocked us on Twitter or it's a private account")

elif choice=='4':
    try:
        print_json()
        print_html()
        print_text_file()
    except:
        print("Thread can be inaccessible because:\nThe thread is too old (we can only retrieve 3200 tweets per user)\nThe thread was deleted on Twitter by the author or by Twitter\nThe Twitter account was deleted by the author or by Twitter\nThe Twitter account was banned/suspended by Twitter\nThe author blocked us on Twitter or it's a private account")

else:
    print("!!Wrong input!!")
    input("press enter to exit")