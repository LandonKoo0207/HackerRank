# Solution for Absolute Permutation
# Problem description at https://www.hackerrank.com/challenges/absolute-permutation/

t = int(input().strip())
for a0 in range(t):
    n,k = map(int, input().split(" "))
    
    # if k = 0, print the numbers from 1 to N as it is.
    # if (n/k) is not even number, there is no absolute permutation, so print -1
    # otherwise, go through the following pattern:
    #  1. permutation is either i+k or i-k. It always starts with i+k
    #  2. Put i+k to the permutation list for k times,
    #  3. Then switch, to put i-k to the permutation list for k times,
    #  - repeat 2 & 3 until the end
    if k == 0:
        print (*list(range(1, n+1)))
    elif (n/k) % 2 != 0:
        print ("-1")
    else:
        add = True
        perm = []
        
        for i in range(1, n+1):
            if add:
                perm.append(i+k)                
            else:
                perm.append(i-k)
                
            if i % k == 0:
                if add:
                    add = False
                else:
                    add = True
        print (*perm)
