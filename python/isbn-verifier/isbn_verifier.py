def is_valid(isbn):
  isbn = isbn.translate( { ord(c):None for c in '- ' })
  if not isbn[:9].isnumeric():
    return False
    
  if len(isbn) != 10:
    return False

  formula = 0
  multiplier = 10
  for i in range(0,9):
    formula += multiplier*int(isbn[i])
    multiplier -= 1

  if isbn[9].isnumeric():
    return (formula+int(isbn[9]))%11==0

  if isbn[9] == 'X':
    return (formula+10)%11==0

  return False