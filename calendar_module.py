from calendar import Calendar

class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, daynum):
        counter = 0
        months = [month for month in range(1, 13)]
        for month in months:
            for data in c.monthdays2calendar(year, month):
                for day in data:
                    if day[1] == daynum and day[0] != 0:
                        counter += 1
        return counter
