import os
import threading
import redis
from .constants import COMMONWORDS
from dotenv import load_dotenv
load_dotenv()
from autocorrect import Speller
spell = Speller()


def search_db(keywords, db_id, db_idx_id):
    db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=db_id)
    db_idx = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=db_idx_id)

    terms = []
    for keyword in keywords:
        if keyword not in COMMONWORDS and db_idx.exists(keyword):
            terms.append(keyword)

        else:
            corrected_keyword = spell(keyword)

            if corrected_keyword != keyword:
                corrected_keywords = corrected_keyword.split()

                for corrected_keyword in corrected_keywords:
                    if corrected_keyword not in COMMONWORDS and corrected_keyword not in STOPWORDS and db_idx.exists(corrected_keyword):
                        terms.append(corrected_keyword)
                        keywords[keywords.index(keyword)] = corrected_keyword

    intersection = [entry.decode("utf-8") for entry in db_idx.sinter(terms)]
    data = []
    if len(intersection) > 0:
        for entry in intersection:
            data.append({
                "data": [d.decode("utf-8") for d in db.zrange(entry, 0, 100)],
                "keywords": terms
            })

        return [{
            "entry": d["data"],
            "keywords": d["keywords"]
        } for d in data], keywords

    threads = []
    for keyword in terms:
        collection = []

        thread = threading.Thread(target=search_db_thread, args=(db_idx, keyword, collection))
        thread.start()
        threads.append([thread, collection])

    entries = {}
    for thread in threads:
        thread[0].join()
        results = thread[1]

        for i in range(1, len(results)):
            entry = results[i]

            if entry not in entries:
                entries[entry] = {
                    "keywords": [results[0]]
                }
            else:
                entries[entry]["keywords"].append(results[0])

    data = []
    for entry in entries:
        data.append({
            "data": [d.decode("utf-8") for d in db.zrange(entry, 0, 100)],
            "keywords": entries[entry]["keywords"]
        })

    return [{
        "entry": d["data"],
        "keywords": d["keywords"]
} for d in data], keywords


def search_db_thread(db_idx, keyword, collection):
    collection.append(keyword)
    collection.extend([entry.decode("utf-8") for entry in db_idx.smembers(keyword)])
