## Soution for Balanced Bracket problem
## Problem description at https://www.hackerrank.com/challenges/ctci-balanced-brackets/

def isBalanced(exp):
    # list of pairs of brackets
    pairs = ["{}", "[]", "()"]
    
    # indicator whether the string has any pair
    pairExist = False
    
    # for the given string(expression),
    # find any pair of brackets, then remove the pair from the string. (used as the parameter for the recursion)
    for p in pairs:
        if p in exp:
            pairExist = True
            if len(exp) > 2:
                idx = exp.find(p)
                exp = exp[:idx] + exp[idx+2:]
    
    # if the given string doesn't have any pair, print NO
    # else, if the string is 2 characters long and it's a pair, print YES
    # otherwise, recursively call the function until the string meets the first 2 conditions. 
    if pairExist == False:
        print ("NO")
    elif len(exp) == 2 and exp in pairs:
        print ("YES")
    else:
        isBalanced(exp)
        
t = int(input().strip())
for a0 in range(t):
    exp = input().strip()
    isBalanced(exp)
