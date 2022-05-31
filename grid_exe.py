# from grid import Grid
# matrix = Grid(3, 3)
# print(matrix)
# for row in range(matrix.get_height()):
#     for column in range(matrix.get_width()):
#         matrix[row][column] = row * column

# print(matrix)
# matrix.get_height()
# matrix.get_width()
# matrix.__getitem__()
# matrix.__getitem__(1)
# matrix.__getitem__(2)[0]
# matrix.__str__()

from grid import Grid
matrix = Grid(3,3)
matrix.random_fill(1,100)
print(matrix)