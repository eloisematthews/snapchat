from datetime import date
from datetime import timedelta

created = input("What date did you create your snapchat account? (e.g. 1 January 2015) ").split()
day = int(created[0])
month = created[1]
year = int(created[2])

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if month in months:
    month = months.index(month) + 1

today = date.today()
created = date(year, month, day)

length = (today - created).days

score = input("What is your snapchat score? ")
score = int(score.replace(',', ''))

average = score // length #double dash rounds down to the nearest integer

print("You have sent and received an average of", average, "snaps per day")
