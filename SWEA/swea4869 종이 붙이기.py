import sys
sys.stdin = open('swea 종이붙이기.txt')
memo = [1,3]
for i in range(2,31):                   #10~300까지의 N의 범위를 주었으니
    memo.append(2*memo[i-2]+memo[i-1])  #30까지 한번에 계산하여 빼서 사용
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    n = N//10
    print(f"#{tc} {memo[n-1]}")
