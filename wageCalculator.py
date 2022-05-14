# WageCalculator.py
from dataclasses import dataclass
@dataclass
class wageCalculator:
    __input_hours:int
    __input_rate:float
    def grossPay(self):
        return (self.__input_hours* self.__input_rate)
    
# Class Implementation
try:
    hours= int(input('Enter number of hours worked: '))
    rate= float(input('Enter hourly pay rate: '))
    wage = wageCalculator(hours, rate)
    pay = wage.grossPay()
    print(pay)
except:
    print('please input valid numbers');