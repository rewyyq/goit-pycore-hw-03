from datetime import datetime, timedelta
def get_upcoming_birthdays(users: list):
    res = []
    today = datetime.today().date()
    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() #convert str to datetime
        user_birthday = user_birthday.replace(year=today.year)
        days_difference = (user_birthday - today).days
        if days_difference <= -3 :               #if birthday was previously in this year, add +1 to year
            user_birthday = user_birthday.replace(year=today.year + 1)
            res.append({"name": user["name"], "congratulation_date": user_birthday.strftime("%Y.%m.%d")})
        if -2 <= days_difference <= 6:           #check if there are birthdays on this week
            current_week_day = user_birthday.weekday()
            if current_week_day == 5:
                new_date = user_birthday + timedelta(days=2)    #if birthday on weekends move it to monday next week
            elif current_week_day == 6:
                new_date = user_birthday + timedelta(days=1)
            else:
                new_date = user_birthday
            res.append({"name": user["name"], "congratulation_date": new_date.strftime("%Y.%m.%d")})
    return res