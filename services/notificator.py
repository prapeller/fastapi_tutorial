import datetime

import requests


def write_notification(email: str, message=""):
    start_time = datetime.datetime.now()
    res = requests.get(url='https://confirmbets.com/blog/5-Best-Books-to-Start-Betting')
    with open("log.txt", mode="a+") as logfile:
        write_time = datetime.datetime.now()
        content = f"\nstarted: {start_time} | writed: {write_time}: notification for {email}: {message} {res.status_code}"
        logfile.seek(0)
        logfile.write(content)
