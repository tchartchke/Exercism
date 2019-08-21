class Matrix(object):
    def __init__(self, matrix_string):
        rows = matrix_string.split('\n')
        mat = []
        for i in rows:
          row_list = i.split(' ')
          
          row_ints = map(int,row_list)

          mat.append(list(row_ints))



        self.mat = mat

    def row(self, index):
        return self.mat[index-1]


    def column(self, index):
        col = []
        for i in range(len(self.mat)):
          col.append(self.mat[i][index-1])
        return col
