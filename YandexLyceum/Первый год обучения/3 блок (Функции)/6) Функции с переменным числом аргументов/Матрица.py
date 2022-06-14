def matrix(n=1, m=1, a=0):
    if n > 1 and m == 1:
        m = n
    return [[a] * m for i in range(n)]
