s = input().strip()
t = input().strip()
k = int(input().strip())

sameCnt = 0
minDel = 0
minApp = 0
possible = False

if s == t:
    if k % 2 == 0 or len(s) + 1 + len(t) == k:
        possible = True
    else:
        possible = False
else:
    #print (len(s), len(t))
    # if s is longer than t,
    # work out how many characters match,
    # so that can obtain the minimum number of characters to be deleted.
    if len(s) >= len(t):
        for i in range(len(t)):
            if s[i] == t[i]:
                sameCnt += 1
            else:
                break
        #print (sameCnt)
        # minimum number of chars to be deleted: length of s - num of chars matching
        minDel = len(s) - sameCnt
        delCnt = 0
        for x in range(1, k+1):
            if len(s) - 2*x + k == len(t) or len(s) - 2*x + k - 1 == len(t):
                delCnt = x
        
        #print ("delCnt:", delCnt)
        
        if delCnt >= minDel:
            possible = True
        else:
            possible = False
        
    else:
        for i in range(len(s)):
            if s[i] == t[i]:
                sameCnt += 1
            else:
                break
        
        minApp = len(t) - sameCnt
        appCnt = 0
        for y in range(1, k+1):
            if len(s) - k + 2*y == len(t):  
                appCnt = y
        
        if appCnt >= minApp:
            possible = True
        else:
            possible = False
            
if possible == True:
    print ("Yes")
else:
    print ("No")
