class Clock(object):
    def __init__(self, hour, minute):
        self.hour = (hour + minute//60) % 24
        self.minute = minute % 60

    def __repr__(self):
        return "{:02d}".format(self.hour)+':'+"{:02d}".format(self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        m = (self.minute + minutes) % 60
        h = (self.minute + minutes) // 60
        self.minute = m
        self.hour = (self.hour + h) % 24
        return self

    def __sub__(self, minutes):
        return self.__add__(-minutes)