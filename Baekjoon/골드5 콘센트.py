# 2**k 의 시간이 필요하다...
# N의 길이의 리스틀 생성해서 2**0 ~ 2**K 까지의 값의 개수를 측정

# 최소시간을 만든다 -> multitap중 젤 작은거에 남은 기기 중 젤 큰 값을 넣는다.
# 멀티탭 재 정렬


N,M = map(int,input().split())
arr= list(map(int,input().split()))
arr.sort(reverse=True)

multitap = [0]*M
for i in range(N):
    multitap[0] +=arr[i]
    multitap.sort(reverse=False)
print(max(multitap))