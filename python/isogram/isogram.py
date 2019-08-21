def is_isogram(string):
  low = string.lower()
  letters = set()
  
  for i in range(len(low)):
    if low[i].isalpha():
      if low[i] not in letters:
        letters.add(low[i])
      else:
        return False

  return True