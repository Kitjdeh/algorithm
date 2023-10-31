#arr = [a,b,c,d,e....]
# arr len가 N PS len 가 r 이라면
# N**r + r자리수의 랭킹
# arr의 각 key 값이 몇 번째인지 체크 하면 편함
# dictionary로 만들어서 하나 계산
arr = list(input())
PS = input()
N = len(arr)
r = len(PS)
Arr = {}
for i in range(N):
    Arr[arr[i]] = i
result = 0
# r자리 패스워드 니까 r-1자리의 패스워드 값들의 합
for i in range(1,r):
    result += N**i
# CDFE라면 A,B의 경우 4자리 경우의 수 + A,B,C의 경우 자리수 .... 1자리 수
for i in range(r):
    result += (Arr[PS[i]]) * (N**(r-i-1))
    result = (result * N + Arr[PS[i]])
result +=1
print(result%900528)
