def factors(value):
  all_factors = []
  
  while value > 1:
    for div in range(2,value+1):
      if value%div == 0:
        all_factors.append(div)
        value //= div
        break
  return all_factors
