def find_anagrams(word, candidates):
  found = []
  for c in candidates:
    if sorted(word.lower()) == sorted(c.lower()):
      if c.lower() == word.casefold():
        continue
      if not c in found:
        found.append(c)
  return found
      