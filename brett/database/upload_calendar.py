import os
import redis
from constants import *
from formatting import *
from dotenv import load_dotenv
load_dotenv()


def prompt():
    print(yellow("[WARNING] Running this script will modify the production database. Continue?"))
    print(green("Y") + " - yes")
    print(red("N") + " - no")
    response = input()

    if response.lower() == "y":
        print(green("[STATUS] Script running."))
        return True
    elif response.lower() == "n":
        print(red("[STATUS] Script exiting."))
        return False
    else:
        return prompt()


def get_calendar():
    import datetime
    import json
    import requests

    today = datetime.date.today()
    start_date = today.replace(year=today.year - 1).isoformat() + "T05:00:00.000Z"
    end_date = today.replace(year=today.year + 5).isoformat() + "T03:59:59.999Z"

    res = requests.post(CAL_URL, json=CAL_REQ(start_date, end_date))
    calendar = json.loads(res.text)

    print(green("[STATUS] Got calendar."))
    return calendar


def get_data(calendar):
    events = calendar["d"]["events"]

    data = []
    for event in events:
        entry = {}

        if not event["name"]:
            print(red("[ERROR] No event name found."))

        if not event["localStartDate"] or not event["localEndDate"]:
            print(red("[ERROR] No date found."))

        entry["name"] = event["name"]
        entry["start"] = event["localStartDate"]
        entry["end"] = event["localEndDate"]

        if event["location"]:
            entry["location"] = event["location"]

        data.append(entry)

    return data


def get_indx(data):
    indx = []
    for entry in data:
        terms = []

        for key in entry:
            key_terms = ["".join(list(filter(lambda c: c in TAG_CHARS, word.lower()))) for word in entry[key].split()]
            key_terms = list(filter(lambda t: t, key_terms))

            terms.extend(key_terms)

        indx.append(terms)

    return indx


def post_data(data):
    db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=0)

    for entry in db.scan_iter("*"):
        db.delete(entry)

    i = 0
    for entry in data:
        db.hset(str(i), mapping=entry)
        i += 1

    print(green("[STATUS] Posted data."))


def post_indx(indx):
    db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=1)

    for entry in db.scan_iter("*"):
        db.delete(entry)

    i = 0
    for entry in indx:
        for term in entry:
            db.sadd(term, i)
        i += 1

    print(green("[STATUS] Posted indexes."))


def run():
    decision = prompt()
    if not decision:
        quit()

    calendar = get_calendar()

    data = get_data(calendar)

    indx = get_indx(data)

    post_data(data)

    post_indx(indx)


run()
