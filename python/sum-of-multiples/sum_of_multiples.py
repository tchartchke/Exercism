def sum_of_multiples(limit, multiples):
  factors = []
    
  for i in multiples:
    if i == 0:
      continue
    m = 1
    while i*m < limit:
      if not i*m in factors:
        factors.append(i*m)
      m += 1

  return sum(factors)