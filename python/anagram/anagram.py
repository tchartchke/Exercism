from itertools import permutations 

def find_anagrams(word, candidates):
  word = word.lower()
  perm = list(permutations(word))
  p_words = []
  for p in perm:
    string = ''.join(p)
    p_words.append(string)

  found = []
  for c in candidates:
    if c.casefold() == word:
      continue
    if len(c) != len(word):
      continue
    if c.casefold() in p_words:
      if c not in found:
        found.append(c)

  return found