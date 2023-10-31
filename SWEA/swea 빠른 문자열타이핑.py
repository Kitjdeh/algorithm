import sys
sys.stdin = open("swea 빠른 문자열타이핑.txt")
T = int(input())
for tc in range(1,T+1):
    A,B = input().split()
# sa -> B로 줄어듬 --> len(B)길이가 1로 줄어들게 됨
#len(B)가 k 번 해당된다면 len(A)가 k*len(B)만큼 줄어들게 된다
    a = len(A)
    b = len(B)
    k = 0
    i = 0
# A의 i번에서 i+b까지가 B와 일치하면 중복을 피하기 위해 i를 i+b+1지점으로 이동
    while i+b<=a:
        if A[i:i+b] == B:
            k += 1
            i +=b
        else:
            i +=1
    print(f"#{tc} {a-k*(b-1)}")