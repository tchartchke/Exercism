class Garden(object):
  flowers = {
    'V': 'Violets',
    'C': 'Clover',
    'R': 'Radishes',
    'G': 'Grass'
  }

  def __init__(self, diagram, students = None):
    if students is None:
      self.students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    else:
      self.students = students

    self.students.sort()
    self.diagram = diagram.split('\n')

  def plants(self, student):
    num = ((self.students.index(student))*2)
    student_plants = [
      self.flowers[self.diagram[0][num]], self.flowers[self.diagram[0][num+1]],
      self.flowers[self.diagram[1][num]], self.flowers[self.diagram[1][num+1]]
      ]

    return student_plants