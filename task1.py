from datetime import datetime
while True:
    try:
        date = input("Write date in this format 'YYYY-MM-DD': ")
        date = datetime.strptime(date, "%Y-%m-%d")          #str to datetime
        break
    except ValueError:          #strptime requires strict format, if wrong format raise ValueError
        print("Wrong input!")

def get_days_from_today(date: datetime):
    current_day = datetime.today()
    res = current_day.toordinal() - date.toordinal()    #.toordinal to get amount of days
    return print(f"{res} days from now to {date}")
get_days_from_today(date)