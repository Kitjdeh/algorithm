#칭호의 개수 N과 출력해야 하는 캐릭터의 개수 M을 준다.
#[칭호, 값] 의 형태로 리스트 설정
#칭호가 여러개 인 경우 가장 먼저 입력된 칭호 하나만 출력
# => 위에서 아래로 if 문 쓰듯 내려간다.
# import sys
# N,M = map(int,sys.stdin.readline().split())
# condition = [0] * N
# result = [0]*M
# for i in range(N):
#     p,q = sys.stdin.readline().split()
#     q = int(q)
#     condition[i] = [p,q]
#
# for i in range(M):
#     data = int(sys.stdin.readline())
#     cnt = 0
#     while cnt < M-1:
#         if data <= condition[cnt][1]:
#             break
#         else:
#             cnt +=1
#     print(condition[cnt][0])




import sys
N,M = map(int,sys.stdin.readline().split())
condition = [0] * N
for i in range(N):
    p,q = sys.stdin.readline().split()
    q = int(q)
    condition[i] = [p,q]
condition.sort(key = lambda x:x[1])
# print(condition)

for i in range(M):
    data = int(sys.stdin.readline())
    left = 0
    right = N-1
    while left <= right:
        mid = (left+right)//2
        if condition[mid][1] >= data:
            right = mid -1
        else:
            left = mid +1
    print(condition[left][0])