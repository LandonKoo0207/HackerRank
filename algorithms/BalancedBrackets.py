def isBalanced(exp):
    pairs = ["{}", "[]", "()"]
    
    pairExist = False
    
    for p in pairs:
        if p in exp:
            pairExist = True
            if len(exp) > 2:
                idx = exp.find(p)
                exp = exp[:idx] + exp[idx+2:]
                       
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
    
