import operator
"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12

#scores based off of game type
def num(dice, n):
  score = 0
  for d in dice:
    if d == n:
      score += n
  return score

def full(dice, n):
  rolls = {}
  for d in dice:
    if d in rolls:
      rolls[d] += 1
    else:
      rolls[d] = 1

  if len(rolls) == 2:
    l = rolls.values()
    if all(elem in l  for elem in [2, 3]):
      return sum(dice)
  return 0
 
def kind(dice, n):
  rolls = {}
  for d in dice:
    if d in rolls:
      rolls[d] += 1
    else:
      rolls[d] = 1
      
  m = max(rolls, key=lambda key: rolls[key])
  if rolls[m] > 3:
    return m*4
  return 0
 
def l_straight(dice, n):
  if all(elem in dice  for elem in [1, 2, 3, 4, 5]):
      return 30
  return 0
 
def b_straight(dice, n):
  if all(elem in dice  for elem in [2, 3, 4, 5, 6]):
      return 30
  return 0
 
def choice(dice, n):
  return sum(dice)
 
def yacht(dice, n):
  if dice.count(dice[0]) == 5:
      return 50
  return 0


def score(dice, category):
  switcher = {
    category: num,
    7: full,
    8: kind,
    9: l_straight,
    10: b_straight,
    11: choice,
    12: yacht
  }
  return switcher[category](dice, category)
  
  #in terms of readability, might be better to just use a bunch of if statements