from datetime import datetime

def get_birthdays_per_week(users):
    current_datetime = datetime.now().date()

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthday_counts = {weekday: [] for weekday in weekdays}

    for user in users:
        for name, date in user.items():
            new_datetime = date.replace(year=current_datetime.year).date()
            difference = new_datetime - current_datetime
            if 0 < difference.days <= 7:
                weekday = weekdays[new_datetime.weekday()]
                birthday_counts[weekday].append(name)

    for weekday, names in birthday_counts.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")

users = [
    {"Oleg": datetime(year=2006, month=7, day=4)}, 
    {"Lera": datetime(year=1993, month=7, day=3)},
    {"Sean": datetime(year=1978, month=7, day=14)},
    {"Kate": datetime(year=1965, month=8, day=5)}
]

get_birthdays_per_week(users)
