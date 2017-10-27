# Solution for The Grid Search
# Problem description at https://www.hackerrank.com/challenges/the-grid-search/

# Get inputs and contruct the Grid, and the Pattern grid.
t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)
    
    matchFound = False
    
    # from top leftmost corner
    # search through the matching pattern in the grid:
    # 1. from the current point(element in the Grid),
    #    See if the first row matches to the Pattern's first row,
    # 2. If the first tow matches, search through N by N area from the current point
    #    and see if the rest of the N * N area matches the Pattern
    # 3. If any match of N by N area is found, print "YES" then break the loop
    # 4. If no match is found after a complete search through the Grid, print "NO"
    for row in range(R-r+1):
        for col in range(C-c+1):
            matchCnt = 0
            if P[0] == G[row][col:col+c]:
                matchCnt += 1
                for i in range(1, r):
                    if P[i] == G[row+i][col:col+c]:
                        matchCnt += 1
                if matchCnt == r:
                    matchFound = True
                    break
        if matchFound == True:
            print ("YES")
            break
    if matchFound == False:
        print ("NO")
