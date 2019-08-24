def saddle_points(matrix):
  points = []
  if matrix == []:
    return [{}]
  cols = len(matrix[0])
  for r in matrix:
    if len(r) != cols:
      raise ValueError("Irregular Matrix")

  # matrix is in row form
  # creating col version
  col = []
  for c in range(len(matrix[0])):
    column = []
    for r in range(len(matrix)):
      column.append(matrix[r][c])
    col.append(column)

  # Checking for Saddle points
  has_points=False
  for r in range(len(matrix)):
    for c in range(len(col)):
      if matrix[r][c] == max(matrix[r]) and matrix[r][c] == min(col[c]):
        points.append({"row":r+1, "column":c+1})
        has_points = True
  if not has_points:
    return [{}]
  return points


  # two loops. one to fixes r, ones that looks c. keep flags and if met then. yah.