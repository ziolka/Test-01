
from datetime import date

person_list = []
day_list = []
week_list = []
x = ""


today = date.today()
print(today)

next_year_day = today.replace(year=2025)
print(next_year_day)

user_list = [
    {"name": "Bill", "birthday": date(1970, 1, 12)},
    {"name": "Jill", "birthday": date(1982, 1, 14)},
    {"name": "Stan", "birthday": date(1963, 4, 1)},
    {"name": "Jan", "birthday": date(1992, 1, 16)},
    {"name": "Joe", "birthday": date(2000, 10, 31)},
    {"name": "Zoe", "birthday": date(2008, 7, 17)},
    {"name": "Kim", "birthday": date(1975, 8, 4)},
    {"name": "Jim", "birthday": date(1985, 11, 20)},
    {"name": "Ann", "birthday": date(1991, 2, 28)},
    {"name": "Liu", "birthday": date(1997, 5, 22)},
    {"name": "Meg", "birthday": date(2003, 1, 5)},
    {"name": "Zeb", "birthday": date(1969, 6, 2)},
    {"name": "Mario", "birthday": date(1944, 3, 2)},
    {"name": "Dario", "birthday": date(1956, 1, 9)},
    {"name": "Zigi", "birthday": date(2001, 11, 3)},
    {"name": "Zibi", "birthday": date(2003, 5, 7)},
    {"name": "Zenon", "birthday": date(1955, 7, 14)},
    {"name": "Leon", "birthday": date(1966, 8, 21)},
    {"name": "Maria", "birthday": date(1977, 12, 8)},
    {"name": "Grazia", "birthday": date(1947, 4, 12)},
    {"name": "Tom", "birthday": date(2013, 2, 15)},
    {"name": "Bob", "birthday": date(1960, 9, 22)},
]

date1 = date(1970, 1, 12)
date2 = date(1969, 6, 2)
period = date1 - date2
print(period)
if 
