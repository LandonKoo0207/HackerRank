from itertools import product

k, m = map(int, input().split(" "))
lists = []
for i in range(k):
    lists.append([int(x)**2 for x in input().split(" ")][1:])

max_s = 0
for p in list(product(*lists)):
    if sum(p) % m > max_s:
        max_s = sum(p) % m
 
print (max_s)
