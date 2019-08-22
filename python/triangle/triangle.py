def equilateral(sides):
  if not triangle_inequality(sides):
    return False
  if sides[0] == sides[1]:
    if sides[1] == sides[2]:
      return True
  return False

def isosceles(sides):
  if not triangle_inequality(sides):
    return False
  if sides[0] == sides[1]:
    return True
  if sides[1] == sides[2]:
    return True
  if sides[0] == sides[2]:
    return True
  return False

def scalene(sides):
  if not triangle_inequality(sides):
    return False
  return not isosceles(sides)

def triangle_inequality(sides):
  for i in range(len(sides)):
    if sides[i] <= 0:
      return False
  sides.sort()
  return sides[0]+sides[1] > sides[2]