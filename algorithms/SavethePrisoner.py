t = int(input().strip())
for i in range(t):
    n, m, s = [int(x) for x in input().strip().split(" ")]
    init_id = s
    id_ptr = init_id
    
    if m % n != 0:
        res_id = s + (m % n) - 1
    else:
        res_id = s + n - 1
    
    if res_id > n:
        res_id -= n
    
    print (res_id)
