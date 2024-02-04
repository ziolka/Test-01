from datetime import datetime


def get_str_date(date):
    print(date)
    print(type(date))
    
    time_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f%z')

    string_date = time_object.strftime('%A %d %B %Y')
    print(string_date)
    print(type(string_date))
    
    return string_date

# 2021-05-27 17:08:34.149Z
# Thursday 27 May 2021