day = [
  ['first','a Partridge in a Pear Tree.'],
  ['second','two Turtle Doves, '],
  ['third','three French Hens, '],
  ['fourth','four Calling Birds, '],
  ['fifth','five Gold Rings, '],
  ['sixth','six Geese-a-Laying, '],
  ['seventh','seven Swans-a-Swimming, '],
  ['eighth','eight Maids-a-Milking, '],
  ['ninth','nine Ladies Dancing, '],
  ['tenth','ten Lords-a-Leaping, '],
  ['eleventh','eleven Pipers Piping, '],
  ['twelfth','twelve Drummers Drumming, ']]


def recite(start_verse, end_verse):
    results = []

    if start_verse > end_verse:
      return "that's not how you sing a song!"

    if end_verse < 1 or start_verse < 1:
      return "Christmas is a lie!"

    for i in range(start_verse, end_verse+1):
      results.append(verse(i-1))
    print("my results ")
    print(results)
    return results

def verse(verse_num):
  whole_verse = "On the "+day[verse_num][0]+" day of Christmas my true love gave to me: "
  if verse_num == 0:
    return whole_verse + day[verse_num][1]
  else:
    for i in range(verse_num, -1, -1):
      if i == 0:
        whole_verse += "and "
      whole_verse += day[i][1]

  return whole_verse

