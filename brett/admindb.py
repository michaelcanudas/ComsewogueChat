import os
import redis
import json

from dotenv import load_dotenv
load_dotenv()

action_choice = None
while action_choice not in ["view", "delete", "sview", "hview"]:
    action_choice = input("Enter 'view' to print an entire database or 'delete' to delete an entire database: ").lower()

db_choice = None
while db_choice not in ["0", "1", "5"]:
    db_choice = input("Enter '0' for URL Database or '1' for Calender Database: ").lower()

    db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=db_choice)

if action_choice == "view":
    for key in db.scan_iter("*"):
        print(key, ": ", json.loads(db.get(key)))
elif action_choice == "delete":
    for key in db.scan_iter("*"):
        db.delete(key)
elif action_choice == "sview":
    for value in db.sscan_iter("events"):
        print(value)
elif action_choice == "hview":
    for value in db.hscan_iter("events"):
        print(value)