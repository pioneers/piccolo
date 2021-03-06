import urllib.request
import io
import datetime
from bs4 import BeautifulSoup

TEST_STUDENT_WORK_SESSIONS_API = "http://localhost:3000/tomorrow_status"
STUDENT_WORK_SESSIONS_API = "http://worksessions.pierobotics.org/tomorrow_status"


def parse_string(string):
    "Translate a session string into a Datetime object and its attendance boolean."""
    time_format = "%m/%d/%Y, %I:%M %p"
    occupied = string[32:] == 'true'

    return datetime.datetime.strptime(string[:20], time_format), occupied


def active_shifts():
    """Return a list of datetime objects when active sessions will begin."""

    jank = True
    if jank:
        soup = BeautifulSoup(open('WorksessionWebsite.htm'), 'html.parser')
    else:
        try:
            u = urllib.request.urlopen(STUDENT_WORK_SESSIONS_API, data=None)
        except urllib.error.URLError:
            u = urllib.request.urlopen(TEST_STUDENT_WORK_SESSIONS_API, data=None)
        f = io.TextIOWrapper(u, encoding='utf-8')
        text = f.read()
        soup = BeautifulSoup(text, 'html.parser')

    attended_datetimes = list()

    for time_slot in soup.body.find_all('div'):
        string = time_slot.contents[0]
        datetime, answer = parse_string(string)
        if not answer:
            attended_datetimes.append(datetime)
    return attended_datetimes

if __name__ == "__main__":
    shift_list = active_shifts()
    for shift in shift_list:
        print(shift)
