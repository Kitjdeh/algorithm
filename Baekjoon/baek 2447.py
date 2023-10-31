def cal(N):
    a= [['*','*','*'],['*',' ','*'],['*','*','*']]
    b = 3
    c =[]

    while N >b:
        c =[]
        n = b
        b = b*3
        for _ in range(3):
            for i in range(n):
                c.append(a[i] * 3)
        for i in range(n, 2*n):
            for j in range(n, 2*n):
                c[i][j] = ' '
        a = c
    for i in range(int(b)):
        print("".join(a[i]))
N = int(input())
cal(N)