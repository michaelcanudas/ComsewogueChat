import os
import time
import redis
import threading

from dotenv import load_dotenv
load_dotenv()

db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=5)
db_idx = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=6)


def union(keywords):
    entries = db_idx.sunion(keywords)
    entries = [entry.decode("utf-8") for entry in list(entries)]

    return entries


def individual(keywords):
    entries = []

    for keyword in keywords:
        entries.extend([entry.decode("utf-8") for entry in db_idx.smembers(keyword)])

    return entries


def individual_threaded(keywords):
    entries = []
    threads = []

    for keyword in keywords:
        collection = []
        thread = threading.Thread(target=lookup_keyword, args=(keyword, collection))
        thread.start()
        threads.append([thread, collection])

    for entry in threads:
        entry[0].join()
        entries.extend(entry[1])

    return entries


def lookup_keyword(keyword, collection):
    collection.extend([entry.decode("utf-8") for entry in db_idx.smembers(keyword)])


def get_time(function, args):
    t0 = time.time()
    for i in range(500):
        function(args)
    t1 = time.time()

    return t1 - t0


print(get_time(union, ["football", "game", "march"]))
print(get_time(individual_threaded, ["football", "game", "march"]))
