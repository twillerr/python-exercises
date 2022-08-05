import requests
site = requests.get("http://www.nytimes.com/")
site_html = site.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(site_html,"html.parser")

title = soup.find_all("h3")
for i in title:
    print(i.contents)
