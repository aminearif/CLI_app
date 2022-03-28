import argparse
import datetime
import requests
import functions

ap = argparse.ArgumentParser(description='Stat About Userbase Growth');
ap.add_argument('StartDate', type=lambda s: datetime.datetime.strptime(s, '%d-%m-%Y'), help='Please enter the start date in this format : DD-MM-YY')
ap.add_argument('EndDate', type=lambda s: datetime.datetime.strptime(s, '%d-%m-%Y'), help='Please enter the end date in this format : DD-MM-YY')
args = ap.parse_args()

def print_date(startDate, endDate):
    userBase = requests.get("http://sam-user-activity.eu-west-1.elasticbeanstalk.com/")
    for date in userBase.json():
        print(functions.format_date(date))
    print(f'Hi, {startDate.strftime("%d-%m-%Y")} , {endDate.strftime("%d-%m-%Y")}')


if __name__ == '__main__':
    print_date(args.StartDate, args.EndDate)

