import redis
import os

from dotenv import load_dotenv
load_dotenv()


def search_db(keywords, id, id_idx):
    db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=id)
    db_idx = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=id_idx)
    
    entries = db_idx.sunion(keywords)
    entries = [entry.decode("utf-8") for entry in list(entries)]

    results = []
    for entry in entries:
        data = db.zrange(entry, 0, 100)
        results.append([d.decode("utf-8") for d in data])

    return results
