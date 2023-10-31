import sys
sys.stdin = open("1일차 - 암호코드 스캔.txt")

def bit_and(i):
    global M
    result = ''
    for t in range(M):
        word = int(i[t],16)
        output = ''
        for j in range(3, -1, -1):
            output += '1' if word & (1 << j) else '0'

        result +=output

    return result
def check_code(a):
    global K
    A=0
    B=0
    for i in range(0,8,2):
        A +=a[i]
    for j in range(1,8,2):
        B +=a[j]
    if (3*A+B)%10 == 0:
        K = A+B
        return K
    else:
        return 0

def cnt_bit(char):
    t = len(char)-1
    cnt = 4
    result = []
    while t:
        rating = [1, 1, 1, 1]
        cnt = 4
        if char[t] =='0':
            t += -1
        else:
            cnt += -1
            rating[cnt] =1
            while (cnt+1) and t :
                if char[t] == char[t-1]:
                    rating[cnt] +=1
                    t += -1
                else:
                    cnt += -1
                    t += -1
            temp = "".join(map(str, rating[1:4]))
            k = 1
            word = code_map.get(temp)
            while word == None:
                k += 1
                for key, value in dict_a.items():
                    new_key = ''
                    for j in range(3):
                        new_key += str(int(key[j])*k)
                    code_map[new_key] = value
                # fuc = "".join(map(str, rating[1:4]))
                word = code_map.get(temp)
            result.append(word)
    return result
code_map = {
    '211':0,
    '221':1,
    '122':2,
    '411':3,
    '132':4,
    '231':5,
    '114':6,
    '312':7,
    '213':8,
    '112':9,
}
dict_a = {
    '211':0,
    '221':1,
    '122':2,
    '411':3,
    '132':4,
    '231':5,
    '114':6,
    '312':7,
    '213':8,
    '112':9,
}

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    ps_code=''
    result_list = []
    ps_list = []
    result = 0
    for i in range(N):
        arr = input()
        t = M-1
        while t:
            if arr[t] == '0':
                t += -1
            else:
                break
        if t != 0 and arr not in result_list:
            result_list.append(arr)
    for i in range(len(result_list)):
        a = bit_and(result_list[i])
        b = cnt_bit(a)[::-1]
        ps_length = len(b) // 8
        for j in range(ps_length):
            if b[j*8:j*8+8] not in ps_list:
                ps_list.append(b[j*8:j*8+8])
    for i in range(len(ps_list)):
        ch_point = check_code(ps_list[i])
        # print(tc,ch_point)
        result +=ch_point
    print(f'#{tc} {result}')

    # result.append(ch_point)
    # print(result)

