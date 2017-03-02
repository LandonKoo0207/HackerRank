# Solution for The Bomberman Game
# Problem description at https://www.hackerrank.com/challenges/bomber-man

r, c, n = map(int, input().split(" "))
grid = []

# construct a new grid with the old grid
def constructNewGrid(old):
    new = [list("O"*c) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if old[i][j] == "O":
                for k in range(max(0, i-1), min(i+2, r)):
                    new[k][j] = "."
                for k in range(max(0, j-1), min(j+2, c)):
                    new[i][k] = "."
    return new

for i in range(r):
    grid.append(list(input()))

# The new grid will always be either one in 3rd second or the other in 5th second.
# i.e. basically the cells around the bombs in the initial grid 
#      are either filled with 'O' or '.' 
# For n > 5,
#     every 4 seconds, each type appears repeatedly.
#     As 3 % 4 == 3, and 5 % 4 == 1, the resulted grid is the following:
#         if n % 4 == 3, then print the grid in 3rd second
#         if n % 4 == 1, then print the grid in 5th second
    
if n == 0 or n == 1:
    for i in range(r):
        print (''.join(grid[i]))
elif n % 2 == 0:
    print ('\n'.join(['O'*c for _ in range(r)]))
else:    
    gridInThird = constructNewGrid(grid)
    gridInFifth = constructNewGrid(gridInThird)
    
    if n == 3:
        resGrid = gridInThird
    elif n == 5:
        resGrid = gridInFifth
    elif n > 5 and n % 4 == 3:
        resGrid = gridInThird
    elif n > 5 and n % 4 == 1:
        resGrid = gridInFifth

    for i in range(r):
        print (''.join(resGrid[i]))
        
