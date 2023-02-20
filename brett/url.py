import os

import requests
import urllib.parse
from bs4 import BeautifulSoup
import redis
import json
from dotenv import load_dotenv
load_dotenv()

db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=0)

checkedURL = []
def parse(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")

    for link in links:
        href = link.get("href")
        title = link.get("title")
        if href.startswith("http"):
            url_components = urllib.parse.urlparse(href)
            subdirectory = url_components.path.split("/")[1] if len(url_components.path.split("/")) > 1 else None
            subdirectory = subdirectory.replace("_"," ")
            subdirectory = subdirectory.replace("-"," ")
            subdirectory = subdirectory.replace("   "," ")

            if isinstance(subdirectory, str):
                subdirectory = subdirectory.title()
            if isinstance(title, str):
                title = title.title()

            db.set(href, json.dumps([subdirectory, title]))
            checkedURL.append(str(href))

urls = ["https://www.comsewogue.k12.ny.us","https://clinton.comsewogue.k12.ny.us","https://norwood.comsewogue.k12.ny.us","https://boyle.comsewogue.k12.ny.us","https://terryville.comsewogue.k12.ny.us","https://jfkms.comsewogue.k12.ny.us","https://comsewoguehs.comsewogue.k12.ny.us"]

for url in urls:
    parse(url)

for key in db.scan_iter("*"):
    if key.decode("UTF-8") not in checkedURL:
        db.delete(key)
        print(str(key) + " was deleted")