date1 = "January 7, 2018"
date2 = "July 7, 2022"
date3 = "March 8, 2028"
date4 = "October 7, 2018"

month = date4.split()[0]
print(month)

seasons = {
    'Зима': 'December January February'.split(),
    'Весна': 'March April May'.split(),
    'Лето': 'June July August'.split(),
    'Осень': 'September October November'.split()
}

for season in seasons:
    if month in seasons[season]:
        print(season)