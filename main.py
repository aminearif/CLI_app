import argparse
import datetime
import requests
import time
import functions

ap = argparse.ArgumentParser(description='Stat About Userbase Growth');
ap.add_argument('StartDate', type=str , help='Please enter the start date in this format : DD-MM-YY')
ap.add_argument('EndDate', type=str , help='Please enter the end date in this format : DD-MM-YY')
args = ap.parse_args()

def print_date(startDate, endDate):
    userBase = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
    jsonUserBase= userBase.json().items()
    dict = {}
    dateStart1 = int(time.mktime(datetime.datetime.strptime(startDate, '%d-%m-%Y').timetuple()))
    dateEnd1 = int(time.mktime(datetime.datetime.strptime(endDate, '%d-%m-%Y').timetuple()))

    for key, value in jsonUserBase :
        dateKey = int(time.mktime(datetime.datetime.strptime(key, '%d-%m-%Y').timetuple()))
        if (dateKey in range(dateStart1,dateEnd1+1)):
            print("dates in range date : ",key , "value : ", value)
            valuedict = value
            dict.update({dateKey : valuedict})
        else:
            print("Date is not in range")

    print("************",dict)


if __name__ == '__main__':
    print_date(args.StartDate, args.EndDate)

