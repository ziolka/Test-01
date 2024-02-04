from datetime import datetime, date


def get_days_from_today(date):
    splitted_date = date.split("-")
    past_date = datetime(year=int(splitted_date[0]), month=int(splitted_date[1]), day=int(splitted_date[2]))
    past_date = past_date.date()
    current_date = datetime.now()
    current_date = current_date.date()
    days_number = current_date - past_date
    result = days_number.days
    
    return result