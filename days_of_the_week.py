class WeekDayError(Exception):
    pass

class Weeker:
    
    cal = {
        0: 'Mon',
        1: 'Tue',
        2: 'Wed',
        3: 'Thu',
        4: 'Fri',
        5: 'Sat', 
        6: 'Sun'
    }

    def __init__(self, day):
        days = {
            'Mon': 0,
            'Tue': 1,
            'Wed': 2,
            'Thu': 3, 
            'Fri': 4,
            'Sat': 5,
            'Sun': 6
        }
        if day not in days.keys():
            raise WeekDayError
        self.__day_num = days[day]

    def __str__(self):
        return self.cal[self.__day_num]

    def add_days(self, n):
        self.__day_num = (self.__day_num + n) % 7
        
    def subtract_days(self, n):
        self.__day_num = (self.__day_num - n) % 7

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
