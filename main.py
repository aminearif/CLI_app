import argparse
import datetime

ap = argparse.ArgumentParser(description='Stat About Userbase Growth');
ap.add_argument('StartDate', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), help='Please enter the start date in this format : DD-MM-YY')
ap.add_argument('EndDate', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'), help='Please enter the end date in this format : DD-MM-YY')
args = ap.parse_args()
def print_date(startDate, endDate):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {startDate} , {endDate}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_date(args.StartDate, args.EndDate)

