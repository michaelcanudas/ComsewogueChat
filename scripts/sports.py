import requests
from bs4 import BeautifulSoup

data = {
  "view": "on",
  "mode": "1",
  "schoolmenu": "COG",
  "leaguemenu": "ALL",
  "sportmenu": "ALL",
  "sportlevelmenu": "ALL",
  "datemenu": "7/1/2022",
  "enddatemenu": "7/1/2023",
  "B1": "Submit"
}
res = requests.post("http://www.sectionxi.org/v3/schedules.asp?menu=", data=data)
soup = BeautifulSoup(res.content, "html.parser").get_text()

print(soup)