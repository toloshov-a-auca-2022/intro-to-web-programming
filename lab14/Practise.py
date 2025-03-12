#1
import calendar

year = 2025
month = 2
print(calendar.month(year, month))

#2
import time
def countdown(seconds):
    while seconds:
        print("Time remaining:", seconds, "seconds.")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
countdown(5)

#3
import time

start = time.time()

sum(range(1, 1000001))

end = time.time()

elapsed = end - start
print(f"Execution Time: {elapsed:.4f} seconds")