from datetime import date
f_date = date.today()
l_date = date(2022, 12, 31)
diff_days = l_date - f_date
print("Number of days remaining are:", diff_days.days)