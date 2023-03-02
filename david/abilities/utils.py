import redis
import os

from dotenv import load_dotenv
load_dotenv()


def search(keywords, id):
    db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=id)

    matches = []
    #for value in db.sscan_iter("events", match="*Meeting*"):
    #    print(value)
        #for keyword in keywords:
        #    if keyword in value:
        #        matches.append(value)

    return []
