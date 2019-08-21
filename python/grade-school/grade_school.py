class School(object):
  def __init__(self):
    self.students = {}
    self.grades = []

  def add_student(self, name, grade):
    if grade in self.grades:
      self.students[grade].append(name)
      self.students[grade].sort()
    else:
      self.students[grade] = [name]
      self.grades.append(grade)
      self.grades.sort()

  def roster(self):
    std = []
    for i in self.grades:
      std += self.students[i]
    return std

  def grade(self, grade_number):
    if grade_number not in self.grades:
      return []
    else:
      return self.students[grade_number]