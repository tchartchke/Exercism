import random, string

class Robot(object):

    def rando_name(self):
      letter1 = str(random.choices(string.ascii_uppercase)[0])
      letter2 = str(random.choices(string.ascii_uppercase)[0])
      num = str("{:03d}".format(random.randint(0,1000)))
      temp_name = letter1+letter2+num
      return temp_name

    def reset(self):
      temp_name = self.rando_name()

      while self.name == temp_name:
        temp_name = self.rando_name()

      self.name = temp_name

    def __init__(self):
      self.name = None
      self.reset()
