import os
import time
import redis
from formatting import *
from dotenv import load_dotenv
load_dotenv()


def prompt():
    print("Enter terms to search.")

    terms = input().split()
    return terms


def search(terms):
    db_data = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=0)
    db_indx = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=1)

    start = time.time()

    results = db_indx.sunion(terms)
    entries = []
    for result in results:
        entries.append(db_data.hgetall(result))

    end = time.time()

    return entries, round(end - start, 4)


def display(entries, elapsed):
    for entry in entries:
        print(entry)

    print(green("[STATUS] Found ") + str(len(entries)) + green(" result(s) in ") + str(elapsed) + green(" seconds."))


def run():
    terms = prompt()

    entries, elapsed = search(terms)

    display(entries, elapsed)


run()
