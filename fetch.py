import requests
import datetime
from errors import ClassNotFoundError, InvalidNumberError
import elementpath
import xml.etree.ElementTree as ET

onl_key = "Online"
base_url = "https://courses.illinois.edu/cisapp/explorer/schedule"

def get_course(subject: str, number: str, crn: str):
    subject = subject.upper()

    if not number.isdigit():
        raise InvalidNumberError(number)
    elif not crn.isdigit():
        raise ValueError(crn)

    year = datetime.datetime.now().strftime("%Y")
    semester = "spring"
    week = int(datetime.datetime.now().strftime("%U"))
    if week > 22:
        semester = "fall"

    url = f"{base_url}/{year}/{semester}/{subject}/{number}/{crn}.xml"
    result = requests.get(url).text

    if len(result) <= 0:
        raise ClassNotFoundError(subject, number, crn)

    root = ET.fromstring(result)
    meetings = root.find("meetings")

    start_date = root.find("startDate").text[:-1] if root.find("startDate") is not None else "N/A"
    end_date = root.find("endDate").text[:-1] if root.find("endDate") is not None else "N/A"

    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")

    if meetings is not None:
        for meeting in meetings.findall("meeting"):
            meeting_type = meeting.find("type").text
            if meeting_type == onl_key:
                print(f"Type: {meeting_type}")
                continue
            start_time = meeting.find("start").text
            end_time = meeting.find("end").text
            days = meeting.find("daysOfTheWeek").text.strip()
            room = meeting.find("roomNumber").text
            building = meeting.find("buildingName").text

            print(f"Type: {meeting_type}")
            print(f"start: {start_time}")
            print(f"end: {end_time}")
            print(f"Days: {days}")
            print(f"Location: {building} {room}")
            print("-" * 40)



get_course("CS", "423", "31378")
get_course("CS", "441", "73205")
