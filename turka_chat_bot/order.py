import datetime
import time
type='default'
size='default'
topping='default'
# filing_time=datetime.datetime.now()

class order:
    def __init__(self,type='default',size='default',topping='default',):
        self.type = type
        self.size = size
        self.topping = topping
        self.hours = 0
        self.min = 0

    def plus_1_hour(self):
        self.hours += 1
        if self.hours > 24:
            self.hours = 1

    def plus_30_min(self):
        self.min += 30
        if self.min >59:
            self.min -=60
            self.plus_1_hour()

    def plus_5_min(self):
        self.min += 5
        if self.min > 59:
            self.min -= 60
            self.plus_1_hour()

    def plus_1_min(self):
        self.min += 1
        if self.min > 59:
            self.min -= 60
            self.plus_1_hour()

    def set_type(self, type):
        self.type = type

    def set_topping(self, topping):
        self.topping = topping

    def set_size(self, size):
        self.size = size

    def reload_time(self):
        time_ = time.localtime()
        self.hours = time_.tm_hour
        self.min = time_.tm_min

    def get_filing_hours(self):
        return self.hours

    def get_filing_min(self):
        return self.min

    def get_full_order(self):
        return f'{self.type} {self.size} Сироп: {self.topping} к {self.hours}:{self.min}'

