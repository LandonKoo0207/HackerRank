# Solution for Queens Attack 2
# Problem description at https://www.hackerrank.com/challenges/queens-attack-2

n,k = map(int, input().strip().split(' '))
rQueen,cQueen = map(int, input().strip().split(' '))

# Every attackable sqaure when there is no obstable
# attackable verticals(row and column)
vertical = (n-1) * 2

# attackable diagonals
upper_left = min(n-rQueen, cQueen-1)
bottom_right = min(rQueen-1, n-cQueen)
upper_right = min(n-rQueen, n-cQueen)
bottom_left = min(rQueen-1, cQueen-1)

# Variables for the number of obstacles
# obstacles in the same row and the column
col_left_obstacle = 0
col_right_obstacle = 0
row_upper_obstacle = 0
row_bottom_obstacle = 0

# obstacles in the diagonal to the queen
# The last element in a tuple indicates whether there is any obstacle in the diagonal direction
diagonal_upper_left = (n,1, False)
diagonal_bottom_right = (1,n, False)
diagonal_upper_right = (n,n, False)
diagonal_bottom_left = (1,1, False)

# Count the attackable squares only when there is any obstacle
# Otherwise print all the attackable squares
if k != 0:
    for a0 in range(k):
        rObstacle,cObstacle = map(int, input().strip().split(' '))

        # For the obstacle is in the same row as the queen
        if rObstacle == rQueen:
            # Count squares in the right side of the queen
            if cObstacle < cQueen:
                if cObstacle > col_left_obstacle:
                    col_left_obstacle = cObstacle
            # Count squares in the left side of the queen
            elif cObstacle > cQueen:
                if n - cObstacle + 1 > col_right_obstacle:
                    col_right_obstacle = n - cObstacle + 1
        # For the obstacle is in the same column as the queen
        elif cObstacle == cQueen:
            # Count squares in the lower side of the queen
            if rObstacle < rQueen:
                if rObstacle > row_bottom_obstacle:
                    row_bottom_obstacle = rObstacle
            # Count squares in the upper side of the queen
            elif rObstacle > rQueen:
                if n - rObstacle + 1 > row_upper_obstacle:
                    row_upper_obstacle = n - rObstacle + 1
                    
        # For the obstacle is in the diagonal to the queen
        else:
            # if the obstacle is not affecting the attackable squares
            # skip the counting
            if abs(rQueen - rObstacle) == abs(cQueen - cObstacle):
                if rObstacle - rQueen > 0:
                    # For obstacles in the diagonal direction, located to the upper of the queen
                    if cObstacle < cQueen:
                        if cObstacle > diagonal_upper_left[1]:
                            diagonal_upper_left = (rObstacle, cObstacle, True)
                    elif cObstacle > cQueen:
                        if cObstacle < diagonal_upper_right[1]:
                            diagonal_upper_right = (rObstacle, cObstacle, True)
                elif rObstacle - rQueen < 0:
                    # For obstacles in the diagonal direction, located to the lower of the queen
                    if cObstacle < cQueen:
                        if cObstacle > diagonal_bottom_left[1]:
                             diagonal_bottom_left = (rObstacle, cObstacle, True)
                    elif cObstacle > cQueen:
                        if cObstacle < diagonal_bottom_right[1]:
                            diagonal_bottom_right = (rObstacle, cObstacle, True)

    # Count the attackable squares in the vertical directions (row and column)
    vertical -= col_left_obstacle + col_right_obstacle + row_bottom_obstacle + row_upper_obstacle

    # Count the attackable squares in the diagonal directions
    # Reduce the count only when there is any obstacle in a dianognal direction
    # otherwise, count all the possible squares in the direction 
    if diagonal_upper_left[2]:
        upper_left -= min(n - diagonal_upper_left[0] + 1, diagonal_upper_left[1])

    if diagonal_bottom_right[2]:
        bottom_right -= min(diagonal_bottom_right[0], n - diagonal_bottom_right[1] + 1)

    if diagonal_upper_right[2]:
        upper_right -= min(n - diagonal_upper_right[0] + 1, n - diagonal_upper_right[1] + 1)

    if diagonal_bottom_left[2]:
        bottom_left -= min(diagonal_bottom_left[0], diagonal_bottom_left[1])

print (vertical + upper_left + bottom_right + upper_right + bottom_left)
