import re

def count_words(sentence):
    sent = sentence.lower()
    split_words = re.findall(r'[a-z]+\'[a-z]+|[a-z]+|\d+', sent)
    counts = {}

    for i in split_words:
      if i in counts:
        counts[i] += 1
      else:
        if len(i)>0:
          counts.update({i:1})
        

    return counts

