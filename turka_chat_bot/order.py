import datetime
import time
type='default'
size='default'
topping='default'
# filing_time=datetime.datetime.now()

class order:
    def __init__(self,type = 'test_type_coffe',type_drink='coffee',size='test_size_coffe',topping='strawberry', milk = 'just'):
        self.type = type
        self.type_drink = type_drink
        self.size = size
        self.topping = topping
        self.hours = 0
        self.min = 0
        self.time = 0
        self.milk = milk


    def set_milk(self, milk):
        self.milk = milk

    def get_milk(self):
        return self.milk



    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type


    def set_type_drink(self, type):
        self.type_drink = type

    def get_type_drink(self):
        return self.type_drink


    def set_topping(self, topping):
        self.topping = topping

    def get_topping(self):
        return self.topping

    def set_size(self, size):
        self.size = size







    def reload_time(self):
        time_ = time.localtime()
        self.hours = time_.tm_hour
        self.min = time_.tm_min

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return time

    def get_filing_hours(self):
        return self.hours

    def get_filing_min(self):
        return self.min

    def get_full_order(self):
        return f'{self.type} {self.size} Сироп: {self.topping} на {self.milk} молоке к {self.hours}:{self.min}'

    def get_full_order_hand_input(self):
        return f'{self.type} {self.size} Сироп: {self.topping} на {self.milk} молоке к {self.time}'

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


