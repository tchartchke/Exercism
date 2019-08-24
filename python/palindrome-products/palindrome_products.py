def find_palindromes(min_factor, max_factor):
  palindromes = {}
  for a in range(min_factor, max_factor+1):
    for b in range(min_factor, max_factor+1):
      mul = a*b
      rev = "".join(reversed(str(a*b)))
      if str(a*b) == rev:
        if a > b:
          a1 = b
          b1 = a
        else:
          a1 = a
          b1 = b  
        item = [a1, b1]
        if mul in palindromes:
          if not item in palindromes[mul]:
            palindromes[mul].append(item)
        else:
          palindromes[mul] = [[a1, b1]]
  return palindromes


def largest(min_factor, max_factor):
  error(min_factor, max_factor)
  pal = find_palindromes(min_factor, max_factor)
  if pal == {}:
    return (None, [])  
  factor = max(pal)
  print(factor, pal[factor])
  return factor, pal[factor]

def smallest(min_factor, max_factor):
  error(min_factor, max_factor)
  pal = find_palindromes(min_factor, max_factor)
  if pal == {}:
    return (None, [])
  factor = min(pal)
  return factor, pal[factor]

def error(min_factor, max_factor):
  if max_factor < min_factor:
    raise ValueError("invalid min/max value")


# ...(..., minormax):
#   if minormax = max:
#     cmp_fn = lambda x,y: x<y
#   else:
#     cmp_fn = lambda x,y: y<x

#   if cmp_fn(curr_min, new_val):
#     ...



# itertools-> products
# check error -> name
# in for, changing simple a/i thing won't break


#for min , if the larger one 

# only use i > j 
# second loop can be based on frist loop