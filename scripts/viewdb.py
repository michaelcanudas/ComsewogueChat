import os
import json
import redis
import requests

from dotenv import load_dotenv
load_dotenv()

req = { "portletInstanceId":"10184","primaryCalendarId":"60310","calendarIds":["60310"],"localFromDate":"2023-02-26T05:00:00.000Z","localToDate":"2023-04-02T03:59:59.999Z","filterFieldValue":"","searchText":"","categoryFieldValue":"","filterOptions":[{"__type":"ModernCalendarDropdownOption","text":"Name","value":"Name"}] }
res = requests.post("https://www.comsewogue.k12.ny.us/Common/controls/WorkspaceCalendar/ws/WorkspaceCalendarWS.asmx/Modern_Events", json=req)
data = json.loads(res.text)

db = redis.from_url(os.getenv("DB_CONN"), ssl_cert_reqs=None, db=0)

# events = data["d"]["events"]