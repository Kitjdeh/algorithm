import sys
sys.stdin =open("220816_string(4).txt")
#str1을 set으로 만든 후 다시 list화 하여 중복을 없앤다
#str1의 i번째의 갯수를 각각 확인하는 count를 쓴ㄴ다
#count가 최대치일 경우 max_count에 넣는다.
T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    str1 = set(str1)
    str1 = list(str1)
    N = len(str1)
    M = len(str2)
    max_count = 0
    for i in range(N):
        count = 0
        for j in range(M):
            if str1[i] == str2[j]:
                count +=1
        if max_count<count:
            max_count =count
    print(f"#{tc} {max_count}")