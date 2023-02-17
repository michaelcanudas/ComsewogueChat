import os
import redis
import json

from dotenv import load_dotenv
load_dotenv()

db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=1)

for key in db.scan_iter("*"):
    print(key, ": ", json.loads(db.get(key)))