# imports datetime from Python built-in datetime
from datetime import datetime # lets you work with date and time
mood = input("How are you feeling right now? : ")

# file handling block
# opens a file called mood_log.txt, if it doesn't exist, Python will be create it
# "a" means append mode (add new contetnt at the end of file without deleting old data)
with open("mood_log.txt", "a") as file: # with...as file: is a context manager (makes sure file get closed automatically after done writing even if an error happends)
    file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {mood}\n") # datetime.now -> gets the current date and time
    # strftime -> string format time (takes a datetime object like 2025-08-21 15:32:10.123456 and turns it into a string (text) in the format that you want)
    # without strftime, datetime.now() will look like this : 2025-08-21 15:32:45.234567 (have microseconds)

print("Mood saved ✅")