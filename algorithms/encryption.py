# Solution for Encryption
# Problem description at https://www.hackerrank.com/challenges/encryption

import math

s = input().strip()

if math.sqrt(len(s)).is_integer():
    cols = int(math.sqrt(len(s)))
else:
    cols = int(math.sqrt(len(s))) + 1

    
for i in range(cols):
    for j in range(len(s)):
        if (j % cols) == i:
            print (s[j], end="")
    print (end=" ")
