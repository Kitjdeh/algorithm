import sys
sys.stdin = open("5203_베이비진 게임_220922_완전검색_그리디.txt")
def triple(arr):                                                    #0~9 인덱스 리스트에 숫자를 입력후 갯수 파악
    global tc
    L = len(arr)
    ch_arr = [0 for i in range(0,10)]
    for i in range(L):
        ch_arr[arr[i]] += 1
    for j in range(10):
        if ch_arr[j] >2:
            return 1
    else:
        return 0

def runrun(arr):                                                       #0~9 인덱스 리스트에 숫자를 입력후 연속성 파악
    L = len(arr)
    ch_arr = [0 for i in range(0,10)]
    for i in range(L):
        ch_arr[arr[i]] = 1
    for i in range(8):
        if ch_arr[i] == 1 and ch_arr[i+1] ==1 and ch_arr[i+2] ==1 :
            return 1
            break
    return 0

T= int(input())
for tc in range(1,T+1):
    card = list(map(int,input().split()))
    a = []
    b = []
    win = 0
    for i in range(12):
        if i % 2 == 0:
            a.append(card[i])
            if runrun(a) or triple(a):
                print(f'#{tc} 1')
                win = 1
                break
        else:
            b.append(card[i])
            if runrun(b) or triple(b):
                print(f'#{tc} 2')
                win = 2
                break
    if win ==0:
        print(f'#{tc} 0')

