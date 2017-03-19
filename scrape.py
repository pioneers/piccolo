import urllib.request
import io
import datetime
from bs4 import BeautifulSoup

TEST_STUDENT_WORK_SESSIONS_API = "http://localhost:3000/tomorrow_status"
STUDENT_WORK_SESSIONS_API = "http://localhost:3000/tomorrow_status"


def parse_string(string):
    time_format = "%m/%d/%Y, %I:%M %p"
    occupied = string[32:] == 'true'

    return datetime.datetime.strptime(string[:20], time_format), occupied


def active_shifts():
    #try:
    #u = urllib.request.urlopen(STUDENT_WORK_SESSIONS_API, data=None)
    #except urllib.error.URLError:
    #        u = urllib.request.urlopen(TEST_STUDENT_WORK_SESSIONS_API, data=None)
    #f = io.TextIOWrapper(u, encoding='utf-8')
    #text = f.read()
    soup = BeautifulSoup(open('WorksessionWebsite.htm'), 'html.parser')

    result = list()

    for shift in soup.body.find_all('div'):
        string = shift.contents[0]
        key, answer = parse_string(string)
        if not answer:
            result.append(key)
    return result

if __name__ == "__main__":
    thing = active_shifts()
    for x in thing:
        print(x)
