# Soultion for Waiter Discussion
# Problem description at https://www.hackerrank.com/challenges/waiter/

# get n primes and return as list
def getPrimes(n):
    primes = []
    
    seq = 0
    isPrime = True
    for i in range(2, 100000):
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
        if isPrime:
            seq += 1
            primes.append(i)
        
        isPrime = True
        
        if seq == n:
            break
     
    return primes

n, q = map(int, input().split(" "))
a0 = [int(x) for x in input().split(" ")]
a = []

# get q prime numbers 
primes = getPrimes(q)

# repeat q iterations:
#    1. if any number is divisible by i th prime, append it to b
#       otherwise, append it to a(temp)
#    2. print numbers in b as an iteration goes.
#    3. append a_temp list to a 
for i in range(q):
    a_temp = []
    b_temp = []
    for j in range(len(a0)-1, -1, -1):
        if a0[j] % primes[i] == 0:
            b_temp.append(a0[j])
        else:
            a_temp.append(a0[j])
    
    for k in b_temp[::-1]:
        print (k)
    
    a.append(a_temp)
    
    a0 = a[-1]

# print a in reversed order
for i in a[-1][::-1]:
    print (i)
