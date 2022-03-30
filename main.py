import argparse
import datetime
import requests
import time
import matplotlib.pyplot as plt
import pandas as pd
import os
from dotenv import load_dotenv

import functions

load_dotenv()
URL= os.getenv('USER_BASE_URL')


ap = argparse.ArgumentParser(description='Stat About Userbase Growth');
ap.add_argument('StartDate', type=str , help='Please enter the start date in this format : DD-MM-YY')
ap.add_argument('EndDate', type=str , help='Please enter the end date in this format : DD-MM-YY')
args = ap.parse_args()

def print_date(startDate, endDate):

    dict = functions.filter_date(startDate, endDate)

    date_time = pd.to_datetime([*dict])
    data = dict.values()

    DF = pd.DataFrame()
    DF['value'] = data
    DF = DF.set_index(date_time)
    plt.plot(DF)
    plt.gcf().autofmt_xdate()
    plt.savefig('plot.png')
    plt.show()


if __name__ == '__main__':
    print_date(args.StartDate, args.EndDate)