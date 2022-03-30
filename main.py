import argparse
import matplotlib.pyplot as plt
import pandas as pd

import functions


ap = argparse.ArgumentParser(description='Stat About Userbase Growth');
ap.add_argument('StartDate', type=str , help='Please enter the start date in this format : DD-MM-YY')
ap.add_argument('EndDate', type=str , help='Please enter the end date in this format : DD-MM-YY')
args = ap.parse_args()

# filter user activity by date range passed as CLI arguments
dict = functions.filter_date(args.StartDate, args.EndDate)

# parse dates & set dataframe
date_time = pd.to_datetime([*dict])
data = dict.values()
DF = pd.DataFrame()
DF['value'] = data
DF = DF.set_index(date_time)

# plot the graph
plt.plot(DF)
plt.title('Userbase Activity')
plt.xlabel('Dates')
plt.ylabel('Active Users')
plt.legend('growth')
plt.gcf().autofmt_xdate()
plt.savefig('plot.png')
plt.show()
