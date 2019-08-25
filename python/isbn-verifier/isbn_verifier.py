import re 

def is_valid(isbn):
  isbn = re.sub(r'[ -]+', '', isbn)

  if not isbn[:9].isnumeric():
    return False
    
  if len(isbn) != 10:
    return False

  total = 0
  multiplier = 10
  for i in range(0,9):
    total += multiplier*int(isbn[i])
    multiplier -= 1

  if isbn[9].isnumeric():
    return (total+int(isbn[9]))%11==0

  if isbn[9] == 'X':
    return (total+10)%11==0

  return False

  # error checking should be done at the beginning
  # for complex forumlas, could simplify equation processing by using variables