import os

import requests
import urllib.parse
from bs4 import BeautifulSoup
import redis
import json
from dotenv import load_dotenv
load_dotenv()

def parse(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")

    pages = []
    for link in links:
        href = link.get("href")
        title = link.get("title")
        if (href.startswith("http")):
            url_components = urllib.parse.urlparse(href)
            subdirectory = url_components.path.split("/")[1] if len(url_components.path.split("/")) > 1 else None
            subdirectory = subdirectory.replace("_"," ")
            subdirectory = subdirectory.replace("-"," ")
            subdirectory = subdirectory.replace("   "," ")
            pages.append((href, title, subdirectory))

            db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=0)
            db.set(href, json.dumps([title, subdirectory]))

urls = ["https://www.comsewogue.k12.ny.us","https://clinton.comsewogue.k12.ny.us","https://norwood.comsewogue.k12.ny.us","https://boyle.comsewogue.k12.ny.us","https://terryville.comsewogue.k12.ny.us","https://jfkms.comsewogue.k12.ny.us","https://comsewoguehs.comsewogue.k12.ny.us"]

for url in urls:
    parse(url)