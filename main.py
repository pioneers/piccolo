import scrape
import datetime
from spreadsheet import sheets
from mail import mail

def main():
    print("beginning Piccolo")
    spreadsheetID = "1lXvP6G-ZuoAXbisdD2imn-hVQffMbdQWD58rkYnxcIc"
    rangeName = "Assignments!A1:H"

    is_weekly_schedule = True
    subject = "It worked"
    attendMessage = "Pls"

    staffAssignments, startDate, endDate = sheets(spreadsheetID, rangeName)

    if is_weekly_schedule:
        if not endDate:
            print("End Date not specified, program will run until manually stopped.")
        else:
            if after(endDate):
                print("Passed end date for session: %s" % endDate)
                return -1

        activeTimes = scrape.active_shifts()
        activeTimesAsString = list()
        for time in activeTimes:
            activeTimesAsString.append(time.strftime("%A %I:%M %p"))

        recipients = set([])
        TIME = 0
        EMAILS = 1
        for activeTimeString in activeTimesAsString:
            for assignment in staffAssignments:
                if activeTimeString == assignment[TIME]:
                    print("%s has active shift at %s" % (assignment[EMAILS], activeTimeString))
                    recipients.update(assignment[EMAILS])

        recipients = ', '.join(list(recipients))
        mail(recipients, "PiE", attendMessage, subject)

    else:
        pass
    print("finishing Piccolo")


def after(endDate):
    return endDate > datetime.datetime.today()

if __name__ == "__main__":
    main()

