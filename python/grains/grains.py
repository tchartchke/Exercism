def square(number):
  error(number)
  return 2**(number-1)

def total(number):
  error(number)
  return (2**(number))-1

def error(number):
  if number <= 0 or number > 64:
    raise ValueError("Invalid square")