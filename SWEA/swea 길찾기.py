import sys
sys.stdin = open("길찾기.txt")
def root(A):
    num = []
    for i in A:
        for j in idx[i]:
            values[j] = True
            num.append(j)
    return num
for tc in range(1,11):
    T,N = map(int,input().split())
    char = list(map(int,input().split()))
    arr = []
    idx = list([]*N for i in range(N))
    for i in range(0,N):                            #경로 리스트화
        arr.append(char[2*i:2*i+2])
    for i in range(N):                              #각 노드에서 갈 수 있는 경로 리스트
        idx[arr[i][0]].append(arr[i][1])
    values = [False] *(100)
    cnt = 0

    k=[0]
    while True:
        if values[99] == True:
            cnt +=1
            break
        elif k == root(k):
            break
        else:
            k = root(k)
    if cnt == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')