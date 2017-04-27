# Solution for Circular Array Rotation
# Problem description at https://www.hackerrank.com/challenges/circular-array-rotation

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

for i in range(k):
    a.insert(0, a.pop())

for a0 in range(q):
    m = int(input().strip())
    print(a[m])
