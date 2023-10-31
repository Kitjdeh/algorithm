#N개의 수에서 i 번째 수 K를 뽑았을 경우 K와 결합하여 만들 수 있는 수는 N-1개
#num_list={}생성
#num_list[K] = 1로 생성
#중복이면 +1
#체크해서 있으면 +num_list[K]
N = int(input())
arr = list(map(int,input().split()))
cnt = 0
num_list={}
add_list=[]
for i in range(N):
    K = arr[i]
    if K not in num_list:
        num_list[K] = 1
    else:
        num_list[K] +=1

for i in range(N):
    K = arr[i]
    for j in range(N):
        T = arr[j]
        if i ==j:
            pass
        else:
            if (K+T) in arr and (K+T) not in add_list:
                cnt +=num_list[K+T]
                add_list.append(K+T)
print(cnt)