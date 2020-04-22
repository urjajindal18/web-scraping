from bs4 import BeautifulSoup
import requests


global count
count=0
def surgeon(flag,url):
  page=requests.get(url)
  soup=BeautifulSoup(page.text,'html.parser')
  if flag==1:
    n=soup.find(class_='name-bar')
    name=(n.find('h1')).contents[0]
    return (name)
  if flag==2:
    contact=soup.find(class_='contact')
    ph=contact.find('a', attrs={'data-contact-type':'Phone'})
    if ph!=None:
        ph=ph.contents[0]
        return (ph)
  if flag==3:
    contact = soup.find(class_='contact')
    email = contact.find('a', attrs={'data-contact-type': 'Email'})
    if email!=None:
        email = email.contents[0]
        return (email)

