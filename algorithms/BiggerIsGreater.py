# Solution for Bigger is Greater
# Problem description at https://www.hackerrank.com/challenges/bigger-is-greater

def nextlexPerm(arr):
    nextPerm = ""
            
    if len(arr) == 2:
        if arr[0] < arr[1]:
            nextPerm = arr[1] + arr[0]
        elif arr[1] > arr[0]:
            nextPerm = arr
        else:
            nextPerm = "no answer"
        print (nextPerm)
    elif arr.count(arr[0]) == len(arr):
        print ("no answer")
    else: 
        first = ""
        for i in range(len(arr)-1, 1, -1):
            # when earlier character is smaller than later character,
            # it is the point where to sort the substring afterwards.
            subStrIdx = None
            if arr[i] > arr[i-1]:
                subStrIdx = i-1
                break
                
        if subStrIdx is None:
            subStrIdx = 0
                
        tmpArr = sorted(arr[subStrIdx:])
        for j in range(len(tmpArr)):
            if tmpArr[j] > arr[subStrIdx]:
                first = tmpArr[j]
                tmpArr.remove(tmpArr[j])
                break
                
        nextPerm = ''.join(arr[:subStrIdx]) + first + ''.join(tmpArr) 
                 
        if nextPerm > ''.join(arr): 
            print (nextPerm)
        else:
            print ("no answer")
                       
t = int(input())
for i in range(t):
    nextlexPerm(list(input()))
