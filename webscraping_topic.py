import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://www.bikewale.com/honda-bikes/")
soup=BeautifulSoup(response.content,'html.parser')

names=soup.find_all('h3',class_='o-jjpuv o-cVMLxW o-mHabQ o-fzpibK')
name=[]
for i in names[0:20]:
    d=i.get_text()
    name.append(d)

prices=soup.find_all('span',class_='o-eZTujG o-byFsZJ o-bkmzIL o-bVSleT')
price=[]
for i in prices[0:20]:
    d=i.get_text()
    price.append(d)

ratings=soup.find_all('p',class_='o-frVjwE o-bdcqVx o-cKuOoN o-lIIwF o-eZTujG')
rating=[]
for i in ratings[0:20]:
    d=i.get_text()
    rating.append(d)

images=soup.find_all('img',class_='o-bXKmQE o-cgkaRG o-cQfblS o-bNxxEB o-pGqQl o-wBtSi o-bwUciP o-btTZkL o-bfyaNx o-eAZqQI')
image=[]
for i in images[0:20]:
    d=i['src']
    image.append(d)

links=soup.find_all('a',class_='o-cpnuEd o-SoIQT o-eZTujG o-fzpilz')
link=[]
for i in links[0:20]:
    d="https://www.bikewale.com"+i['href']
    link.append(d)

df=pd.DataFrame() #row columns
df["Names"]=name
df["Prices"]=price
df["Ratings"]=rating
df["Images"]=image
df["Links"]=link

df.to_csv("Bikes.csv")