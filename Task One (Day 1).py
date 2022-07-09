#Import the datetime module
#Determining the date
from datetime import date
date = date.today()

#Getting the weekday
week_num = date.weekday()
week_days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
day = (week_days[week_num])
print("Date: ",date)
print("Day: ",day)

#Determining the fare on each day
if week_num == 0 or week_num == 1 or week_num == 2 or week_num == 3 or week_num == 4:
    fare = 100
elif week_num == 5:
    fare = 60
else:
    fare = 80
    
print("Fare:",fare)
