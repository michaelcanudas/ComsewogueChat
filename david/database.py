import redis
import os

from dotenv import load_dotenv
load_dotenv()

def search(keywords,num):
    db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=num)
    valid_strings = []
    for key in db.keys('*'):
        value = db.get(key)
        if value and keywords in value.decode('utf-8').lower():
            valid_strings.append(key.decode('utf-8'))
    return valid_strings