#Datetime

#1. Getting the Current Date and Time
from datetime import datetime

now = datetime.now()
print("Current date and time:", now)

#2. Extracting Specific Parts of a Date
from datetime import datetime

print("Year:", datetime.now().year)
print("Month:", datetime.now().month)
print("Day:", datetime.now().day)
print("Hour:", datetime.now().hour)
print("Minute:", datetime.now().minute)
print("Second:", datetime.now().second)

#3. Creating a Specific Date and Time
from datetime import datetime

specificDate = datetime(2023, 12, 31, 23, 59, 59)
print(specificDate)


#4. Formatting Dates and Times (strftime)
from datetime import datetime

formattedDate = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print("Formatted Date:", formattedDate)


#5. Parsing Strings into Date Objects (strptime)
from datetime import datetime

dateStr = "05-02-2025 09:19:23"
dateObj = datetime.strptime(dateStr, "%d-%m-%Y %H:%M:%S")
print("Parsed Date Object:", dateObj)


#6. Performing Date Calculations (timedelta)
from datetime import datetime, timedelta

futureDate = datetime.now() + timedelta(days=5)
print("Future Date in 5 days:", futureDate)

pastDate = datetime.now() - timedelta(days=5)
print("Past date:", pastDate)


#7. Finding the Difference Between Two Dates
from datetime import datetime

eventDate = datetime(2025, 12, 12)
daysRemaining = eventDate - datetime.now()

print("Days until event:", daysRemaining.days)