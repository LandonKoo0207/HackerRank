# Solution for Ema's Supercomputer
# Problem description at https://www.hackerrank.com/challenges/two-pluses

n, m = map(int, input().split(" "))
grid = []
first_grid = []
validPluses = []

# Function getting all the possible valid pluses
# Get a grid as an input and size
# and then add the pluses with the size.
def getValidPlus(grid, size):
    if size == 0:
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "G":
                    validPluses.append((i, j, 0))
    else:                
        for i in range(n):
            for j in range(m):
                cntLeft = cntRight = cntUpper = cntBelow = 0
                plus_area = 0

                if grid[i][j] == "G":
                    if i != 0 and j != 0 and i != n-1 and j != m-1:
                        for k in range(i, max(i-size-1, -1), -1):
                            if grid[k][j] == 'G':
                                cntUpper += 1
                            else:
                                break
                        for k in range(i, min(i+size+1, n)):
                            if grid[k][j] == 'G':
                                cntBelow += 1
                            else:
                                break
                        for k in range(j, max(j-size-1, -1), -1):
                            if grid[i][k] == 'G':
                                cntLeft += 1
                            else:
                                break
                        for k in range(j, min(j+size+1, m)):
                            if grid[i][k] == 'G':
                                cntRight += 1
                            else:
                                break

                        if cntLeft == cntRight == cntUpper == cntBelow == size+1:
                            validPluses.append((i, j, size))

# Function that take two pluses and check if they overlap.
# if they overlap, return True
# otherwise, return False
# - Build each grid with a centre cell, 
#   then see if any cells overlap
def overlap(plus1, plus2):
    i1, j1, s1 = plus1
    i2, j2, s2 = plus2
    
    firstPlus = []
    secondPlus = []
    
    for v in range(i1 - s1, i1 + s1 + 1):
        firstPlus.append((v, j1))
    for h in range(j1 - s1, j1 + s1 + 1):
        firstPlus.append((i1, h))
    
    for v in range(i2 - s2, i2 + s2 + 1):
        secondPlus.append((v, j2))
    for h in range(j2 - s2, j2 + s2 + 1):
        secondPlus.append((i2, h))
    
    overlap = False
    for pair in firstPlus:
        if pair in secondPlus:
            overlap = True
            break
    
    if overlap:
        return True
    else:
        return False

# Build the grid of 'G' and 'B'
for i in range(n):
    grid.append(input())

# Get the maximum possible plus size
# - size here is the length FROM the centre cell
#   (e.g. if size is 2, this means the plus has 2 cells to each of the upper, below, left and right )
# - if the smallest of the row and column is even number, 
#    the maximum size is the smallest / 2 - 1
#   otherwise, it is the smallest / 2
if min(m, n) % 2 == 0:
    maxPlusSize = int(min(m, n) / 2 - 1)
else:
    maxPlusSize = int(min(m, n) / 2)

# All of the possible pluses 
for i in range(maxPlusSize+1):    
    getValidPlus(grid, i)

# All of the sizes of the valid pluses
sizes = []
for i in range(len(validPluses)):
    sizes.append(validPluses[i][2])

# All of the possible unique products of the two pluses.
# Store as tuples: (first plus size, second plus size, the product)
products = [(1, x*4+1, x*4+1) for x in set(sizes)]
if len(set(sizes)) == 1:
    plusSize = sizes[0]*4 + 1
    if sizes.count(sizes[0]) > 1:
        if (plusSize, plusSize) not in products:
            products.append((plusSize, plusSize, plusSize**2))
else:
    for i in set(sizes):
        plusSize = i*4 + 1
        if sizes.count(i) > 1:
            if (plusSize, plusSize) not in products:
                products.append((plusSize, plusSize, plusSize**2))
        for j in set(sizes):
            if i != j:
                anotherPlus = j*4 + 1
                if (plusSize, anotherPlus) not in products and (anotherPlus, plusSize) not in products:
                    products.append((anotherPlus, plusSize, anotherPlus*plusSize))

# sort the valid pluses by size
# sort the products by products
# - to search the valid pair of pluses from the pair with the largest product possible.
validPluses = sorted(validPluses, key=lambda plus: plus[2], reverse=True)
products = sorted(products, key=lambda prod: prod[2], reverse=True)

# Find the two largest pluses with the largest product
# Check from the larest pair and see if they DO NOT overlap
# if they don't overlap, print the product of two
# otherwise, keep searching until the next largest two are found.
pairFound = False
i = 0
while pairFound == False:
    for p1 in range(len(validPluses)):
        p1size = validPluses[p1][2] * 4 + 1
        if p1size == products[i][0]:
            for p2 in range(len(validPluses)):
                if p1 != p2:
                    p2size = validPluses[p2][2] * 4 + 1
                    if p2size == products[i][1]:
                        if overlap(validPluses[p1], validPluses[p2]) == False:
                            print (products[i][2])
                            pairFound = True
                            break
            if pairFound:
                break
    i += 1
