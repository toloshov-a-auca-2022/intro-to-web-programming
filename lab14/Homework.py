#1
from datetime import datetime

now = datetime.now()

from datetime import datetime
eventDate = datetime(datetime.now().year, 12, 31)
now = datetime.now()
daysRemaining = eventDate - now
print("Days Remaining to New Year:", daysRemaining.days)

#2
import time
def countdown(seconds):
    while seconds > 0:
        print("Seconds remaining:", seconds)
        time.sleep(1)
        seconds -= 1

a = int(input("Enter a countdown seconds: "))
countdown(a)
print("Time is up!")


#3
import calendar

def monthCalendar(year, month):
    print(calendar.month(year, month))

while True:
    try:
        year = int(input("Enter the year: "))
        if year == 0: # 0 is a sign of end input
            break

        if year < 0:
            raise ValueError("Year cannot be negative. Please try again.\n")
        month = int(input("Enter the month: "))
        if month < 1 or month > 12:
            raise ValueError("Invalid input of month, must be between 1 - 12. Please try again.\n")
    except ValueError as e:
        print(e)
        continue

    print()
    monthCalendar(year, month)