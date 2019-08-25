import re

class Phone(object):
  def __init__(self, phone_number):
    number = re.sub(r'[-\s+.\(\)]+', r'', phone_number)

    if not number.isnumeric():
      raise ValueError("Not all numbers")
    if len(number) < 10:
      raise ValueError("Not enough numbers")
    if len(number) > 11:
      raise ValueError("Too many numbers")
    if len(number) == 11:
      if number[0] != '1':
        raise ValueError("Bad Country Code")
      number = number[1:]

    if int(number[0]) <2 :
      raise ValueError("Bad Area Code")
    if int(number[3]) <2 :
      raise ValueError("Exchange Code")

    self.number = number

    self.area_code = number[:3]
    self.exchange = number[3:6]
    self.subscriber = number[6:]

  def pretty(self):
    return '({}) {}-{}'.format(self.area_code, self.exchange, self.subscriber)