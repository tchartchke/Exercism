def factors(value):
  all_factors = []
  
  while value > 1:
    for div in range(2,value+1):
      if value % div == 0:
        all_factors.append(div)
        value //= div
        break
  return all_factors

# keep a current value that can be incremented because if it's not d
# divisible by 2, it'll never be divisible by 2 aagain