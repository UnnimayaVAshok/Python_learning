from datetime import datetime, timedelta

#date and times
current_time = datetime.now()
print("Today : " + str(current_time))

one_day = timedelta(days = 1)
yesterday = current_time - one_day
print("Yesterday : "+ str(yesterday))

one_week = timedelta(weeks = 1)
last_week = current_time - one_week
print("Last week : "+ str(last_week))

#stripping content
Birth_input = input("Enter your birthday dd/mm/yyyy")
Birth_day = datetime.strptime(Birth_input,"%d/%m/%Y")
Birth_date = Birth_day.day
Birth_month = Birth_day.month
Birth_year = Birth_day.year
print("Date : " + str(Birth_date))
print("Month : " + str(Birth_month))
print("Year :" + str(Birth_year))