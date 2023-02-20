import os
import json
import redis
import requests
import datetime
import re
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv()

today = datetime.date.today()
start = today.replace(year=today.year - 1)
end = today.replace(year=today.year + 5)

startISO = start.isoformat() + "T05:00:00.000Z"
endISO = end.isoformat() + "T03:59:59.999Z"

startSTR = start.strftime("%B %d, %Y")
endSTR = end.strftime("%B %d, %Y")

def formatinfo(list):
    for i in range(len(list)):
        if isinstance(list[i], str) and i != 2:
            list[i] = list[i].title()
            if " Hs " in list[i] or list[i].startswith("Hs ") or list[i].endswith(" Hs"):
                list[i] = list[i].replace("Hs", "High School")
    return list




req = { "portletInstanceId":"10184","primaryCalendarId":"60310","calendarIds":["60310"],"localFromDate":startISO,"localToDate":endISO,"filterFieldValue":"","searchText":"","categoryFieldValue":"","filterOptions":[{"__type":"ModernCalendarDropdownOption","text":"Name","value":"Name"}] }
res = requests.post("https://www.comsewogue.k12.ny.us/Common/controls/WorkspaceCalendar/ws/WorkspaceCalendarWS.asmx/Modern_Events", json=req)
data = json.loads(res.text)

db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=1)

def newDates(datesString, newDate, name):
    dates = [datetime.datetime.strptime(date, "%B %d, %Y") for date in datesString.split("; ")]
    new_date = datetime.datetime.strptime(newDate, "%B %d, %Y")
    date_strs = [date.strftime("%B %d, %Y") for date in dates]
    if newDate not in date_strs:
        dates.append(new_date)
        dates.sort()
        return "; ".join([date.strftime("%B %d, %Y") for date in dates])
    else:
        return datesString

events = data["d"]["events"]
checkedID = []
for e in events:
    id = e["eventID"]
    if e["isAllDay"] == True:
        info = [e["name"], e["preformatted_localStartDate"], "All Day", e["location"]]
    else:
        info = [e["name"], e["preformatted_localStartDate"], e["preformatted_localStartTime"], e["location"]]
    if db.get(id) == None:
        for item in info:
            if isinstance(item, str):
                item = item.title()
        db.set(id, json.dumps(formatinfo(info)))
    elif json.loads(db.get(id)) != info:
        index = info.index(e["preformatted_localStartDate"])
        if id in checkedID and info[index] != json.loads(db.get(id))[index]:
            info[index] = newDates(json.loads(db.get(id))[index], info[index], str(e["name"]))
            db.set(id, json.dumps(formatinfo(info)))
        elif id in checkedID or info[index] not in json.loads(db.get(id))[index]:
            db.set(id, json.dumps(formatinfo(info)))
        elif info[index] in json.loads(db.get(id))[index] and any(info[i] != json.loads(db.get(id))[i] for i in range(len(info)) if i != index):
            db.set(id, json.dumps(formatinfo(info)))
    checkedID.append(id)



data = {"view": "on","mode": "1","schoolmenu": "COG","leaguemenu": "ALL","sportmenu": "ALL","sportlevelmenu": "ALL","datemenu": startSTR,"enddatemenu": endSTR,"B1": "Submit"}
res = requests.post("http://www.sectionxi.org/v3/schedules.asp?menu=",data=data)
soup = BeautifulSoup(res.content, "html.parser").get_text()

def isDateValid(dateString):
    dateFormat = re.compile(r'^\d{1,2}/\d{1,2}/\d{4}')
    return bool(dateFormat.match(dateString))

def removeBlanks(string):
    lines = string.replace("\r", "")
    lines = lines.split("\n")
    lines = [line for line in lines if not (line.lstrip().startswith("(") and line.strip().endswith(")"))]
    lines = [line for line in lines if line and line.strip() != '@' and line.strip()]

    index = 0
    while index < len(lines):
        date = lines[index]
        backup = lines[index - 1]
        if isDateValid(date) or isDateValid(backup):
            index += 7
        else:
            del lines[index]
            index = 0

    return "\n".join(line.lstrip().strip() for line in lines)


def groupData(string):
    lines = string.split("\n")
    lines = [line for line in lines if line.strip()]
    sublists = []
    i = 1
    j = 0
    while i < len(lines):
        if isDateValid(lines[i]):
            sublist = lines[j:i]
            j = i
            sublists.append(sublist)
        i += 1
    return sublists

raw, sep, void = soup.partition('Total Contests')
void, sep, raw = raw.partition('Contest Location')
raw = removeBlanks(raw)
data = groupData(raw)

for sublist in data:
    sublist.pop(5)
    if sublist[4].startswith('V'):
        sublist[4] = sublist[4].replace('V', 'VARSITY', 1)
    elif sublist[4].startswith('JV'):
        sublist[4] = sublist[4].replace('JV', 'JUNIOR VARSITY', 1)
    elif sublist[4].startswith('B'):
        sublist[4] = sublist[4].replace('B', 'MIDDLE SCHOOL', 1)
    first_element = str(sublist[0]).replace("/", "_")
    first_element = str(first_element).replace(" ", "")
    fifth_element = sublist[4].title().replace(" ", "")
    newList = fifth_element + first_element
    title = sublist[4].strip().lstrip() + ": " + sublist[2].strip().lstrip() + " @ " + sublist[3].strip().lstrip()
    date = datetime.datetime.strptime(sublist[0], '%m/%d/%Y').strftime('%B %d, %Y')
    if len(sublist) == 6: sublist = [title,date,sublist[1],sublist[5]]
    else: sublist = [title,date,sublist[1],""]
    globals()[newList] = sublist
    checkedID.append(newList)
    db.set(newList, json.dumps(formatinfo(sublist)))



for key in db.scan_iter("*"):
    try:
        if json.loads(key) not in checkedID:
            print("Deleted " + str(key))
            db.delete(key)
    except (TypeError, json.decoder.JSONDecodeError):
        if key.decode("UTF-8") not in checkedID:
            print("Deleted " + str(key))
            db.delete(key)