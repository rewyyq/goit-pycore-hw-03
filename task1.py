from datetime import datetime
def get_days_from_today(date: str) -> int:
    current_day = datetime.today()
    try:
        date = datetime.strptime(date, "%Y-%m-%d") #strptime requires strict format, if wrong format raise ValueError
    except ValueError:          
        return "Wrong date format!"
    res = current_day.toordinal() - date.toordinal()    #.toordinal to get amount of days between dates
    return res