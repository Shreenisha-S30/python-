import calendar

day= int(input("Enter day:"))
month=int(input("enter month:"))
year=int(input("Enter year:"))
day_number=calendar.weekday(year,month,day)
day_name=calendar.day_name[day_number]
print(f"The day on {day}/{month}/{year} is {day_name}")