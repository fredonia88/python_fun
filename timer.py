class Timer:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        hour = str(self.__hours).zfill(2)
        minute = str(self.__minutes).zfill(2)
        second = str(self.__seconds).zfill(2)
        
        return hour + ':' + minute + ':' + second

    def next_second(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self.__hours == 23:
                    self.__hours = 0
                else: 
                    self.__hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1
            

    def prev_second(self):
        if self.__seconds == 0:
            self.__seconds = 59
            if self.__minutes == 0:
                self.__minutes = 59
                if self.__hours == 0:
                    self.__hours = 23
                else: 
                    self.__hours -= 1
            else:
                self.__minutes -= 1
        else:
            self.__seconds -= 1

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
