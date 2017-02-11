def isBalanced(exp):
    # The conditions that are ALWAYS NOT balanced ("NO")
    # - When the following conditions are NOT MET, then the given expression is BALANCED.
    # 1: the length is 1
    # 2: the first character is "close" bracket
    #    the length is odd 
    # 3: the last character is "open" bracket
    # 4: the expression has anything "unpaired" brackets: "(]", "(}", "[)", "[}", "{)", "{]"
    if len(exp) == 1:
        return "NO"
    
    if exp[0] in "}])":
        return "NO"

    if len(exp) % 2 > 0:
        return "NO"
    
    endIdx = len(exp) - 1
    if exp[endIdx] in "{[(":
        return "NO"
    
    if exp.count("{") != exp.count("}"):
        return "NO"
        
    if exp.count("[") != exp.count("]"):
        return "NO"
        
    if exp.count("(") != exp.count(")"):
        return "NO"
        
    if "(]" in exp or "(}" in exp or "[)" in exp or "[}" in exp or "{)" in exp or "{]" in exp:
        return "NO"
    
    return "YES"
        
t = int(input().strip())
for a0 in range(t):
    exp = input().strip()
    print (isBalanced(exp))
    
