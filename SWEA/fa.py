import sys
sys.stdin =open("220816_string(4).txt")
# str1 에서 1글자 2글자 ,, 순으로 늘리고 일치한다면 다음 글자로 넘어가서 일치하지 않을 경우
# 증가된 숫자만큼을 출력
T = int(input())
for tc in range(1,T+1):
    str1 = input()
    L1 = len(str1)
    str2 = input()
    L2 = len(str2)
    #가장 많은 글자 확인
    k = 0
    #글자의 길이가 k일 경우 일치하는 문장이 있는지 L2-k번 확인한다.
    #일치하는게 한번이라도 나오면 바로 for 문 종료
    #k에 1을 더한 후 다시 반복
    #한번도 나오지 않는다면 모든 반복문 종료
    for i in range(L1):
        k +=1
        count = 0
        for j in range(0,L2-k+1):
            if str1[:k] == str2[j:j+k]:
                break
            else:
                count +=0
        if count == L2-k+1:
            break
    print(k)
