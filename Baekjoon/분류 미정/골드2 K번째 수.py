# (1~N)*(1~N) => 오름타순 정렬
# A를 만들어서 정렬..? => 미친짓
# 확실한점 => B[1] = 1, B[N] = N**2
# B배열의 k번째 수 =>
# B[k]번째수 => k번째로 작은수
# 1. N*N 배열 A에서 0~N 배열에서 자기보다 작은 수가 있는지 판단
# N이 6일 경우 10이 몇번째인가??
# [1, 2, 3, 4, 5, 6] => 10보다 작은 수 6
# [2, 4, 6, 8, 10, 12] => 10보다 작은수 5
# [3, 6, 9, 12, 15, 18] => 10보다 작은 수 3
# [4, 8, 12, 16, 20, 24] => 10보자 작은 수 2
# [5, 10, 15, 20, 25, 30] => 10보다 작은수 2
# [6, 12, 18, 24, 30, 36] => 10보다 작은수 1
# 6+4+3+2+1+1 => 17번째 수
# II. f(int,k) 함수 정희
# 2-1. mid = (1,N)//2
# 2-2. mid 가 몇번째인지 확인
# 2-3. mid 가 t 번째 일 경우
# 2-4. k 보다 작으면 mid = (mid+end)//2
# 2-5. k 보다 크면 mid = (1+mid)//2

N = int(input())
K = int(input())
Tree = [0]*(N**2+1)
arr = [[0]*N for _ in range(N)]
start,end = 1,N
mid = (start + end) // 2

while start <=end:
    temp = 0
    for i in range(1,N+1):
        p = min(mid//i,N)
        temp +=p
        if i > mid:
            break
    if temp <= K:
        answer = mid
        start = mid +1
    elif temp > K:
        end = mid - 1
    mid = (start+end)//2
    print(temp,mid)

print(mid,temp,answer)
# 6 7
# 8 6
# 8 5
# 6 5
# 5 6