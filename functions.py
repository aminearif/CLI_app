import datetime
import requests
import time
import matplotlib.pyplot as plt
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
URL= os.getenv('USER_BASE_URL')

def format_date(data):
    return datetime.strptime(data, '%d-%m-%Y')

def filter_date(startDate, endDate):
    # Request user base
    userBase = requests.get(URL)
    jsonUserBase = userBase.json().items()
    dict = {}

    # convert date to timestamp for comparing purposes
    dateStart1 = int(time.mktime(datetime.datetime.strptime(startDate, '%d-%m-%Y').timetuple()))
    dateEnd1 = int(time.mktime(datetime.datetime.strptime(endDate, '%d-%m-%Y').timetuple()))

    for key, value in jsonUserBase:
        dateKey = int(time.mktime(datetime.datetime.strptime(key, '%d-%m-%Y').timetuple()))
        if (dateKey in range(dateStart1, dateEnd1 + 1)):
            valuedict = value
            dict.update({dateKey: valuedict})

    return dict

