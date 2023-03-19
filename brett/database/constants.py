DB_DATA = 0
DB_INDX = 1

CAL_URL = "https://www.comsewogue.k12.ny.us/Common/controls/WorkspaceCalendar/ws/WorkspaceCalendarWS.asmx/Modern_Events"
CAL_REQ = lambda start, end: {
    "portletInstanceId": "116380", "primaryCalendarId": "1029956", "calendarIds": ["1029956"],
    "localFromDate": start, "localToDate": end,
    "filterFieldValue": "", "searchText": "",
    "categoryFieldValue": "", "filterOptions": [
        {"__type": "ModernCalendarDropdownOption", "text": "Name", "value": "Name"}
    ]
}

TAG_CHARS = "abcdefghijklmnopqrstuvwxyz"
