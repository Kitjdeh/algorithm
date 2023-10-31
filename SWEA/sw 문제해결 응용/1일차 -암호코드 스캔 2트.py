# import sys
# sys.stdin = open("1일차 - 암호코드 스캔.txt")
code_map = {
    '3211':0,
    '2221':1,
    '2122':2,
    '1411':3,
    '1132':4,
    '1231':5,
    '1114':6,
    '1312':7,
    '1213':8,
    '3112':9
}
def bit_and(i):                                         #알파벳과 숫자를 정수로 변환
    global M
    result = ''
    for t in range(M):
        word = int(i[t],16)
        output = ''
        for j in range(3, -1, -1):
            output += '1' if word & (1 << j) else '0'
        # print(word, output)

        # while output[0] == '0':
        #     output=output[1::]
        #     if output == '0':
        #         break
        # # print(word, output)
        result +=output
    return result

def cnt_bit(char):                                      #변환된 이진수를 4개씩 끊어서 해석
    t = M-1                                             #뒤에서 부터 진행하니 index를 len-r
    result = []
    print(t)
    while t:
        rating = [1, 1, 1, 1]
        cnt = 4
        if char[t] =='0':                               #4단위의 마지막은 무조건 1이니 0이면 다른것임
            t += -1
        else:
            cnt += -1
            rating[cnt] =1
            while (cnt+1) and t:
                print(rating)
                if char[t] == char[t-1]:
                    rating[cnt] +=1
                    t += -1
                else:
                    cnt += -1
                    t += -1
                if cnt <0:
                    sum = 0
                    for i in range(4):
                        sum +=rating[i]
                    rate = sum//7
                    if rate > 1:
                        for i in range(4):
                            rating[i] = rating[i]//rate
            rating = rating[::-1]
            print(rating)
            word =code_map.get("".join(map(str,rating)))
            print(word)
            result.append(word)
    return result

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    ps_line=''
    for i in range(N):
        arr = input()
        if ps_line != '':
            continue
        t = M-1
        while t:
            if arr[t] == '0':
                t += -1
            else:
                break
        if (t != 0) and ps_line != arr:
            ps_line = arr
            ps_bit = bit_and(ps_line)
            print(ps_bit)
            cnt_bit(ps_bit)
