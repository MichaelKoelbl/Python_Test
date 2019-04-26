import requests
from bs4 import BeautifulSoup
import datetime
page = requests.get("https://climate.nasa.gov/vital-signs/carbon-dioxide/")
soup = BeautifulSoup(page.content,'html.parser')
x = soup.find("div", {"class": "value"})
#x.text
x = x.text.replace('\n', '').replace('\r', '')
now = datetime.datetime.now()

day = now.day
month = now.month
year = now.year

print("The carbon dioxide conentration in the athmosphere today,",year,month,day, " is: ", x)