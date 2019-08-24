class Phone(object):
  def __init__(self, phone_number):
    number = phone_number.translate( { ord(c):None for c in '()-+ \n\t\r' })

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
      
    
    # replace on whitespace string.replace(r"\w", "") and paratenteses and = nad +


# print str.translate(trantab, 'xm')
    # [\w_\+\(\)-]