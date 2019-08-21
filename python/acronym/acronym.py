import re

def abbreviate(words):
  abbr = ''

  full_words = re.findall(r'[A-Z]+\'[A-Z]+|[A-Z]+', words.upper())
  for i in full_words:
    abbr += i[0]

  return abbr

