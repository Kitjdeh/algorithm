#모든 경우 중 제일 싼 경로로 가야함
#12개월의 이용계획을 각 경우로 확인
#재귀함수로 풀어야함
#
def f()
import sys
sys.stdin = open('220930 수영장.txt')
T = int(input())
for tc in range(1,T+1):
    daily,month,three_month,year = map(int,input().split())
    arr = list(map(int,input().split()))
