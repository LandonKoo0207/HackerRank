# Solution for Oranising Containers of Balls
# Problem description at https://www.hackerrank.com/challenges/organizing-containers-of-balls/

# The balls can only be swapped, meaning the number of balls in each container will remain unchanged.
# Therefore, the numbers of balls in containers must be aligend with the numbers of balls of each type
# e.g. For example, if there are 3 containers containing 3, 6, 9 balls,
# then there must be 3 balls of one type, 6 balls of another type and 9 balls of the other type.

q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    M = []
    for M_i in range(n):
        M_t = [int(M_temp) for M_temp in input().strip().split(' ')]
        M.append(M_t)
    
    rowSums = []
    colSums = []
    
    # Get sums of each row (number of balls in each container)
    for i in range(n):
        rowSums.append(sum(M[i]))
    
    # Get sums of each column (number of balls of each type)
    for i in range(n):
        colSum = 0
        for j in range(n):
            colSum += M[j][i]
        colSums.append(colSum)
    
    # if sorted sums are the same, print Possible
    # otherwise, print Impossible
    if sorted(rowSums) == sorted(colSums):
        print ("Possible")
    else:
        print ("Impossible")
