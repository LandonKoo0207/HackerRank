# Solution for Almost Sorted
# Problem description at https://www.hackerrank.com/challenges/almost-sorted/ 

# take 2 indices of the list
#  and swap the numbers of them and return the modified list.
def swap(i, j):
    ret = d[0:]
    temp = ret[i]
    ret[i] = ret[j]
    ret[j] = temp
    
    return ret

# take a list and,
#   return True if sorted, False if not sorted.
def isSorted(lst):
    if sorted(lst) == lst:
        return True
    else:
        return False

n = int(input())
d = [int(x) for x in input().split(" ")]

# Algorithm using stored indices of unordered numbers in the list
# 1. Find unordered numbers in the list
#        then store its indices into a list
# 2. If only 1 index is stored in the list,
#        swapping the 2 adjacent numbers. 
#        swap the numbers and check if it is sorted.
#        if it is sorted, print "yes", and "swap" and the two positions of the numbers in the next line
#        otherwise, print "no"
# 3. If the stored list has more than 1 index,
#        check if the indices are consecutive - e.g. 2,3,4,5: consecutive, 1,3,5,7: non-consecutive
#        if it is consecutive, reverse the numbers with the indices,
#          and check if the numbers are sorted.
#          if it is sorted, print "yes" and the "reverse" and the start position and end position of the reversed numbers in the next line.
#        if it is non-consecutive, 
#           i) and there are more than 2 indices, print "no".
#           ii) and there are 2 indices, print "swap" and the two positions of the numbers in the next line  

unordered = []
for i in range(len(d)-1):
    if d[i] > d[i+1]:
        unordered.append(i)

if len(unordered) == 1:
    ret = swap(unordered[0], unordered[0]+1)
    if isSorted(ret):
        print ("yes")
        print ("swap", unordered[0]+1, unordered[0]+2)
    else:
        print ("no")
else:
    isCons = True
    for i in range(len(unordered)-1):
        if unordered[i] + 1 != unordered[i+1]:
            isCons = False    

    if isCons:
        temp = d[unordered[0]:unordered[len(unordered)-1]+2][::-1]
        if isSorted(d[:unordered[0]] + temp + d[unordered[len(unordered)-1]+2:]):
            print ("yes")
            print ("reverse", unordered[0]+1, unordered[len(unordered)-1]+2)
        else:
            print ("no")
    else:
        if len(unordered) > 2:
            print ("no")
        else:
            ret = swap(unordered[0], unordered[1]+1)
            if isSorted(ret):
                print ("yes")
                print ("swap", unordered[0]+1, unordered[1]+2)
            else:
                print ("no")
