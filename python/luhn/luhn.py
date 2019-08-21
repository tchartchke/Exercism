class Luhn(object):
  
  def __init__(self, card_num):
    card_string = card_num.replace(" ","")
    if card_string.isnumeric():
      self.card_num = card_string
    else:
      self.card_num = None

    print(card_string)

  def valid(self):
    if self.card_num is None or len(self.card_num) < 2:
      return False
    else:
      card = [int(i) for i in self.card_num]
      for i in range(len(card)-2, -1, -2):
        card[i] *= 2
        if card[i] > 9:
          card[i] -= 9
    if sum(card) % 10 == 0:
      return True
    return False
