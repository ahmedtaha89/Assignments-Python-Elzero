# تكليفات الدروس من الدرس 079 إلى 080

# التكليف 01

import datetime
date1 = datetime.datetime(2021, 6, 25)
date2 = datetime.datetime(2021, 8, 10)
print(f"Days From {datetime.datetime(2021, 6, 25)} To {datetime.datetime(2021, 8, 10)} Is => {(date2-date1).days}")


# التكليف 02
day = datetime.datetime.now() 

print(day.strftime("%Y-%m-%d"))      # "2023-08-04"
print(day.strftime("%b %d, %Y"))     # "Aug 04, 2023"
print(day.strftime("%d - %b - %Y"))  # "04 - Aug - 2023"
print(day.strftime("%d / %b / %y"))  # "04 / Aug / 23"
print(day.strftime("%d / %B / %Y"))  # "04 / August / 2023"
print(day.strftime("%a, %d %M %Y"))    # "Fri, 04 27 2023"

