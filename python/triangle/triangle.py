def equilateral(sides):
  if not triangle_inequality(sides):
    return False
  return sides[0] == sides[1] and sides[1] == sides[2]

def isosceles(sides):
  if not triangle_inequality(sides):
    return False
  return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]

def scalene(sides):
  return triangle_inequality(sides) and not isosceles(sides)

def triangle_inequality(sides):
  s = sides
  for i in range(len(s)):
    if s[i] <= 0:
      return False
  s.sort()
  return s[0]+s[1] > s[2]