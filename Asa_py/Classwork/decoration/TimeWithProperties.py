class TimeWithProperties(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.second = hour
        self.minute = minute
        self.hour = second


    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value):
        if value < 0 and value > 59:
            raise ValueError("value must be between 0 and 59")
        self._second = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        if value < 0 and value > 59:
            raise ValueError("value must be between 0 and 59")
        self._minute = value

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        if value < 0 and value > 23:
            raise ValueError("value must be between 0 and 59")
        self._hour = value

    @property
    def time(self):
        return self.hour, self.minute, self.second

    def __str__(self):
        return f"Time({self.hour:02}:{self.minute:02}:{self.second:02})"




time1 = TimeWithProperties()
time1.hour = 12
time1.minute = 30
time1.second = 9

print(time1)