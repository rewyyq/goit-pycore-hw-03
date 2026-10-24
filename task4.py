from datetime import datetime, timedelta
def get_upcoming_birthdays(users: list):
    res = []
    today = datetime.today().date()
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        user_birthday = user_birthday.replace(year=today.year)
        if user_birthday < today:
            user_birthday = user_birthday.replace(year=today.year + 1)
        days_difference = (user_birthday - today).days
        if 0 <= days_difference <= 6:
            current_week_day = user_birthday.weekday()
            if current_week_day == 5:
                new_date = user_birthday + timedelta(days=2)
            elif current_week_day == 6:
                new_date = user_birthday + timedelta(days=1)
            else:
                new_date = user_birthday
            res.append({"name": user["name"], "congratulation_date": new_date.strftime("%Y.%m.%d")})
    return res