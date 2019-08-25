def classify(number):
  if number <= 0:
    raise ValueError("Invalid number")
  if number == 1:
    return "deficient"

  num = number
  s = 1
  div = 2

  while num > div:
    if number % div == 0:
      num = number//div
      s += (div + num)
    
    div += 1
    


  if s == number:
    return "perfect"

  if s > number:
    return "abundant"

  return "deficient"


# check code or the factors
#  only have o go up to sqrt(n) (inclusive)