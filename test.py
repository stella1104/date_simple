
from date import date_simple as ds

dateobj1 = get_date()                      # datetime.date object for today
print(dateobj1)

datestr1 = ds.format_date(dateobj1)        # formated string for today
print(datestr1)

datestr2 = ds.format_date(dateobj1,format='MM/DD/YYY')   # formated string ('MM/DD/YYY') for today
print(datestr2)

date_add_day = ds.add_day(dateobj1,1)   # one more day from today
print(date_add_day)

date_add_week = ds.add_week(dateobj1,1)   # one more week from today
print(date_add_week)

date_add_month = ds.add_month(dateobj1)   # one more month from today
print(date_add_month)

date_add_year=ds.add_year(dateobj1)      # one more year from today
print(date_add_year)

dateobj2 = ds.get_date(dt='bad date')    # raises a ValueError exception

datestr3 = ds.format_date(dt=not_a_date_object) # raises a TypeError exception

datestr4 = ds.format_date(dt=dateobj2, format='unrecognized format') # raises a ValueError exception

