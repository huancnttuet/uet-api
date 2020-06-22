

from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import time
from . import uet_news, fcm_notify

scheduler = BackgroundScheduler()
news = uet_news.get_studentnews()

print(news)


def job_function():
    global news
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    temp = uet_news.get_studentnews()
    k = 0
    for t, n in zip(temp, news):
        if t != n:
            fcm_notify.send_notify("Tin tức sinh viên", t[0], "webview", t[2])
            k = 1
    if k == 1:
        news = temp


def start_job():
    global scheduler
    try:
        scheduler.add_job(func=job_function, trigger="interval",
                          seconds=60*15, id='my_job_id')
        scheduler.start()

        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())
    except:
        print("warning :v")


def stop_job():
    global scheduler
    scheduler.remove_job('my_job_id')
