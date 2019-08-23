def steps(number):  
  if number <= 0:
    raise ValueError("invalid input")

  if number == 1:
    return 0

  if number%2 ==0 :
    return 1+steps(number/2)

  return 1+steps(3*number+1)


