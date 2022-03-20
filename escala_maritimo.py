import datetime
from datetime import timedelta

scale = int(input("Enter the number of days of your scale: "))

date_entry = input('Enter the date of your next shipment (AAAA-MM-DD): ')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)

td = timedelta(scale)

num_months = int(input("For how many months do you want to know the scale??: "))

for i in range(1, num_months, 2):
    print("Next landing : ", date1 + (i * td))
    print("Next shipment : ", date1 + ((i+1) * td))