# Solution for Matrix Layer Rotation
# Problem description at https://www.hackerrank.com/challenges/matrix-rotation-algo

# Rotate the given matrix in anti-clockwise
def rotate(matrix):
    col = len(matrix[0])
    row = len(matrix)
    # Rotate the cells in the left most column to downwards
    temp_left_col = matrix[-1][0]
    for i in range(row-1, 0, -1):
        matrix[i][0] = matrix[i-1][0]

    # Rotate the cells in the bottom row to right
    temp_bottom_row = matrix[-1][-1]
    for i in range(col-1, 0, -1):
        matrix[-1][i] = matrix[-1][i-1]
    matrix[-1][1] = temp_left_col

    # Rotate the cells in the right most column to upwards
    temp_right_col = matrix[0][-1]
    for i in range(row-1):
        matrix[i][-1] = matrix[i+1][-1]
    matrix[row-2][-1] = temp_bottom_row

    # Rotate the cells in the right most column to upwards
    for i in range(col-1):
        matrix[0][i] = matrix[0][i+1]
    matrix[0][col-2] = temp_right_col

    return matrix

# Get the inner matrix of the provided matrix
def inner_matrix(matrix):
    row = len(matrix) - 2
    col = len(matrix[0]) - 2

    # while row > 2 and col > 2:
    #     row -= 2
    #     col -= 2
    #     start_idx += 1

    new_matrix = [matrix[i][1:col+1] for i in range(1, row+1)]

    return new_matrix

# Determine whether the given matrix has inner layer
# if it has any, return True
# if it has none, return False
def has_inner(matrix):
    if len(matrix) >= 2:
        if min(len(matrix), len(matrix[0])) >= 2:
            return True
    return False

# Combine rotated inner matrix with the whole matrix
# Replace the cells' contents in the original matrix with those in the rotated inner layer
def combine_inner(original, inner):
    start_idx = (min(len(original), len(original[0])) - min(len(inner), len(inner[0]))) // 2

    for i in range(len(inner)):
        if i == 0 or i == len(inner) - 1:
            for j in range(len(inner[0])):
                original[i+start_idx][j+start_idx] = inner[i][j]
        else:
            original[i+start_idx][start_idx] = inner[i][0]
            original[i+start_idx][start_idx+len(inner[0])-1] = inner[i][-1]

    return original

m, n, r = map(int, input().split(" "))

a = [[int(x) for x in input().split()] for x in range(m)]

num_of_rotations = r
temp_a = a
# Rotate each layer until it reaches the inner most layer of the matrix
while has_inner(temp_a):
    outer_cells = (len(temp_a[0]) * 2) + ((len(temp_a)-2) * 2)
    # Depending on the size of matrix,
    #    Rotated matrices will be repeated.
    #       - num_of_rotations = r % (The column size * 2) + (The row size - 2) * 2
    #       - every num_of_rotations, matrices shown will be repeated.
    #       - therefore, the matrix has the maximum unique rotations as calculated above.
    #       - if r(rotation given in the input) is less than the maximum possible unique rotations, rotate r times as it is.
    if r > outer_cells:
        num_of_rotations = r % ((len(temp_a[0]) * 2) + ((len(temp_a)-2) * 2))
    else:
        num_of_rotations = r

    #print (temp_a)

    # rotate the current layer of the matrix
    for i in range(num_of_rotations):
        temp_a = rotate(temp_a)

    # if the layer is the outer most, just rotate the outer most
    # otherwise, it is a inner layer, so only rotate the inner part of the matrix
    if temp_a == a:
        a = temp_a
    else:
        a = combine_inner(a, temp_a)

    # Get a inner layer of the current layer of the matrix
    temp_a = inner_matrix(temp_a)

# print the rotated matrix
for i in range(len(a)):
    print (*a[i])
