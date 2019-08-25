class Allergies(object):
  __a = ['cats', 'pollen', 'chocolate', 'tomatoes', 'strawberries', 'shellfish', 'peanuts', 'eggs']
  
  def __init__(self, score):
    # makes all the 1010101s
    b = bin(score)[2:]
    if len(b) > 8:
      b = b[(len(b)-8):len(b)]
    self.score = '{:08}'.format(int(b))


  def allergic_to(self, item):
    return item in self.lst

  @property
  def lst(self):
    allergies = []
    for i in range(len(self.score)-1, -1, -1):
      if self.score[i] == '1':
        allergies.append(self.__a[i])
    # self.allergies = allergies
    return allergies


# reversed