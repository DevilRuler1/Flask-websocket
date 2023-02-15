def fib(n):
    if n == -1:
        count = -1
    else:
        count = 1
        
    n1, n2 = 0, 1
    while count <= n:
        yield n1
        n1, n2 = n2, n1 + n2
        
        if n != -1:
            count += 1
    