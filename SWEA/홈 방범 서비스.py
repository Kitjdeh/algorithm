import sys
sys.stdin = open('홈방범서비스.txt')

def guard_area(t):                                  #K의 길이가 t 일때 arr[i][j]에서의 방범 범위 좌표 변화량값 측정
    cir=[]
    for k in range(1,t):
        for i in range(-k+1,k):
            if i !=k-1 and i != -k+1:
                cir.append([i,k-abs(i)-1])
                cir.append([i,-k+abs(i)+1])
            else:
                cir.append([i,0])
#  k =2n-3
    return cir
result = []

for i in range(1,23):                               # N=20(max)일때 정사각형을 모두 포함하는 K=38까지 다 구해놓는다.
    result.append(guard_area(i))
# print(result[3])
# [[0, 0], [-1, 0], [0, 1], [0, -1], [1, 0], [-2, 0], [-1, 1], [-1, -1], [0, 2], [0, -2], [1, 1], [1, -1], [2, 0]]

T =int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_house = 0
    for t in range(N+2):                          # N의 정사각형을 포함하는 최소한의 K값 = 2n-3
        for i in range(N):
            for j in range(N):
                house=0
                for a in result[t]:
                    ni,nj = i+a[0],j+a[1]           # 변화량 투입
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                        house +=1
                if (house*M) >= len(result[t]) and max_house < house:
                    max_house = house
    print(f'#{tc} {max_house}')
# def make_delta(k):
#     delta = [[0, 0]]
#     temp_lst = list(range(k)) + list(range(-1, -k, -1))  # 0 1 2 -1 -2
#     for i in range(len(temp_lst)):
#         for j in range(i, len(temp_lst)):
#             if [temp_lst[i], temp_lst[j]] not in delta and abs(temp_lst[i]) + abs(temp_lst[j]) < k:
#                 delta.append([temp_lst[i], temp_lst[j]])
#             if [temp_lst[j], temp_lst[i]] not in delta and abs(temp_lst[i]) + abs(temp_lst[j]) < k:
#                 delta.append([temp_lst[j], temp_lst[i]])
#     return delta
#
#
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     dosi = [list(map(int, input().split())) for _ in range(N)]
#
#     big_delta = [[] * (N + 2) for _ in range(N + 2)]
#     for i in range(1, N + 2):
#         big_delta[i] = make_delta(i)
#
#     compare = []
#     for i in range(N):
#         for j in range(N):
#             for k in range(1, N + 2):
#                 cost = -(k ** 2 + (k - 1) ** 2)
#                 house = 0
#                 for di, dj in big_delta[k]:
#                     ni = i + di
#                     nj = j + dj
#                     if 0 <= ni < N and 0 <= nj < N and dosi[ni][nj] == 1:
#                         house += 1
#                         cost += M
#
#                 if cost >= 0:
#                     compare.append(house)
#
#     print(f'#{tc + 1} {max(compare)}')