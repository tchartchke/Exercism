def square(number):
  error(number)
  return 2**(number-1)

def total(number):
  error(number)
  sum = 0
  for n in range(1, number+1):
    sum += square(n)
  return sum

def error(number):
  if number <= 0 or number > 64:
    raise ValueError("Invalid square")

# can do sum faster because math a^n