import os
import time

period = 15 # how many minutes
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

while True:
    notify("Bruxism Reminder", "Stop clenching your teeth!")
    print("Press Ctrl+C to exit the program")
    time.sleep(period*60)
