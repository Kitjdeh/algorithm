import sys

sys.stdin = open('색칠하기2.txt')
T = int(input())
for t in range(1,T+1):
    N = int(input())
    # arr[12][12]형태이고 -- 상하좌우 비교하여 둘레의 길이를 측정해야하기에 길이를 늘림
    # 0으로 되어있으나 red칸은 1 blue칸은 2 교집합은 0으로 표시
    arr =[]
    a =[0]
    arr = [[0] * 12 for i in range(12)]
    for _ in range(N):
        x1,y1,x2,y2,c = list(map(int,input().split()))
        x1 +=1
        y1 +=1
        x2 +=1
        y2 +=1
    #c=1 일 경우 red인 1을 행렬에 대입 이미 2가있으면 0으로
        if c == 1:
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    arr[i][j] +=1
    # c=2 일 경우 blue인 2를 행렬에 대입 이미 1이 있으면 0으로
        if c == 2:
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    arr[i][j] +=2
    #red(1)의 둘레는 red한칸(=1)상하좌우의 값이 1과 다르면 1씩 추가된다.
    red_count=[]
    blue_count=[]
    for i in range(12):
        for j in range(12):
            if arr[i][j] ==1:
                red_count.append([i,j])
            elif arr[i][j] ==2:
                blue_count.append([i,j])
    len_r = 0
    len_b = 0
    for a in red_count:
        x = a[0]
        y = a[1]
        if arr[x-1][y] != 1:
            len_r +=1
        if arr[x+1][y] != 1:
            len_r +=1
        if arr[x][y-1] != 1:
            len_r +=1
        if arr[x][y+1] != 1:
            len_r +=1
    for a in blue_count:
        x = a[0]
        y = a[1]
        if arr[x-1][y] != 2:
            len_b += 1
        if arr[x+1][y] != 2:
            len_b += 1
        if arr[x][y-1] != 2:
            len_b += 1
        if arr[x][y+1] != 2:
            len_b += 1
    print(len_b+len_r)

