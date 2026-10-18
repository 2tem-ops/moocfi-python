from datetime import datetime, timedelta

day, month, year = int(input("Day: ")), int(input("Month: ")), int(input("Year: "))

user = datetime(year, month, day)
millennium = datetime(2000, 1, 1)

difference = millennium - user

if difference.days > 0:
    print(f"You were {difference.days - 1} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")