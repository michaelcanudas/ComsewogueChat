import requests
from bs4 import BeautifulSoup

res = requests.get("URL")
soup = BeautifulSoup(res.content, "html.parser")

rows = soup.find_all("tr")
for row in rows:
  print(row)