def factors(value):
  all_factors = []
  
  curr_divisor = 2
  while value > 1:
    for div in range(2,value+1):
      if value % div == 0:
        all_factors.append(div)
        value //= div
        break
      else:
        curr_divisor += 1
  return all_factors