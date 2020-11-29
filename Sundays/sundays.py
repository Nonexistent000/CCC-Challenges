# Written by Syed Muhammad Zafar Alam
# Coded in Python
# Nov. 29 / 2020

#checks for leap years
def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
         return True 
    return False

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
week_days = ["Sunday", "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday"]
count = 0 # number of Sundays
start_point = week_days[5] # sets the start of Jan. 1, i.e. Tuesday

for i in range(1901, 2001):
    if leap_year(i) == True:
        month_days[1] = 29
    else:
        month_days[1] = 28
    
    for month in month_days:
        r = month % 7
        if r == 1:
            start_point = start_point # if remainder is 1, meaning number of days in month is divisible by 7, remain the same start point
        else: 
            start_point = week_days[week_days.index(start_point)-r] # if remainder isn't 1, subtract from start point
        if start_point == "Sunday":
            count += 1

print(count)


