import requests
import time
from bs4 import BeautifulSoup
import pandas as pd
import threading
lock = threading.Lock()

sleep_sec = 1

def get_page(url):
    print(url)
    lock.acquire()

    r = requests.get(url)
    time.sleep(sleep_sec)

    lock.release()

    return BeautifulSoup(r.text,features='lxml')

def get_dataframe(url):
    print(url)

    lock.acquire()

    time.sleep(sleep_sec)
    r = pd.read_html(url)

    lock.release()
    return r
