

T = int(input())
for tc in range(1,T+1):
    N = int(input())
#N*N의 배열을 만든 후 숫자 0으로 채운다
#(0,0)에서 출발하는 a를 만들고
#index 값에따라 방향을 정하고 이동한 만큼의 숫자를 채운다
    arr_a = [0]*N
    arr = []
    for i in range(N):
        arr.append(arr_a)
    x = 0
    y = 0
    c = 1
    arr[x][y] = c
    for i in range(N*N):
        if x ==N:


    #x,y가 우,하,좌,상 순서로 index 확인 후 이동하면서 arr의 값을 추가함

