# Solution for Largest Rectangle
# Problem description at https://www.hackerrank.com/challenges/largest-rectangle/

n = int(input())
h = [int(x) for x in input().split(" ")]

# For each element(height) of an array,
# 1. Search the continuous buildings to the left
#    - if continous building is at the same height or taller, increment the count
# 2. Seach the continuous buildings to the right
#    - if continous building is at the same height or taller, increment the count
# 3. Calculate the current rectangle area: 
#    - height of the current building * current count
# 4. Check if the current area is larger than the current maximum area
# When the search finishes print the maximum area acquired.
max_area = 0
for i in range(len(h)):
    cnt = 0
    for j in range(i, -1, -1):
        if h[j] >= h[i]:
            cnt += 1
        else:
            break
    for k in range(i+1, len(h)):
        if h[k] >= h[i]:
            cnt += 1
        else:
            break
    area = h[i] * cnt
    if area > max_area:
        max_area = area

print (max_area)
