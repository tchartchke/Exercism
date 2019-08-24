def square_of_sum(number):
  s = 0
  for i in range(number, 0, -1):
    s += i
  return s**2

def sum_of_squares(number):
  s = 0
  for i in range(number, 0, -1):
    s+= i**2
  return s


def difference_of_squares(number):
    return(square_of_sum(number) - sum_of_squares(number))


# could do concurrently so loop doesn't run twice if super large number