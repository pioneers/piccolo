import scrape
import datetime
from spreadsheet import sheets
from mail import mail

def main():
    spreadsheetID = "1lXvP6G-ZuoAXbisdD2imn-hVQffMbdQWD58rkYnxcIc"
    rangeName = "Assignments!A1:H"

    is_weekly_schedule = True
    subject = "It worked"
    cancelMessage = "Sorry cancelled"
    attendMessage = "Pls"

    staffAssignments, startDate, endDate = sheets(spreadsheetID, rangeName)

    if is_weekly_schedule:
        if not endDate:
            print("End Date not specified")
            return -1

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
                    recipients.update(assignment[EMAILS])

        recipients = ', '.join(list(recipients))
        mail(recipients, "PiE", attendMessage, subject)


    else:
        pass
    print("finished")


def after(endDate):
    return False

if __name__ == "__main__":
    main()

