
#1. 입력값 내림차순 정렬
#2. 콘센트 중에 제일 시간 적은 놈에 시간 많은놈 +
#3. 콘센트 정렬
N,M = map(int,input().split())
arr= list(map(int,input().split()))
arr.sort(reverse=True)

multitap = [0]*M
for i in range(N):
    multitap[0] +=arr[i]
    multitap.sort(reverse=False)
print(max(multitap))

