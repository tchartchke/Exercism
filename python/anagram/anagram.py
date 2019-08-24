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

  # def find_anagrams(word, candidates):
  #   return[candidate for candidate in candidates 
  #          if (word.lower() != candidate.lower() and sorted(candidate.lower()) == sorted(word.lower()))]


# for loop looks for iterators. itertools returns iterator
  # p_words = []
  # for p in permutations(word):
  #   string = ''.join(p)
  #   p_words.append(string)


# map{lambda}instead of first forloop

# check is uppwer or lower actually changes original string

# set to list conversion
# set and map have constant look up time



# check if sets are equal if saved in locations. can use set operations, set equality
# can python do multisets
