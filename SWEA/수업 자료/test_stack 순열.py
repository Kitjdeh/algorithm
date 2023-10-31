def f(i,N):
    global price

    if i ==N:                       #순열 완성
        print(P)
    else:
        for j in range(i,N):        #P[i]에 들어갈 숫자 결정
            P[i],P[j] = P[j], P[i]

            f(i+1,N)
            P[i],P[j] = P[j],P[i]
P=[0,1,2]
bit = [0]*3
price = 0
f(0,3)
