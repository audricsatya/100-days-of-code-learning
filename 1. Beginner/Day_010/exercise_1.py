# Leap Year and Days in Month Exercise
# Instructions
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, while a leap year has 366 days. This is how you can tell the difference:
# 1. On every year that is evenly divisible by 4
# 2. If the year is evenly divisible by 100, it isn't a leap year
# 3. The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "This is an Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
if is_leap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
print(f"{days} days in month {month} of year {year}.")
