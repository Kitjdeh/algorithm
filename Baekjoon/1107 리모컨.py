A = input().strip()
L = len(A)
N = int(A)
M = int(input())
num =[]
if M==0:                                    #고장난게 없을 경우
    err =[]
else:
    err = list(map(int,input().split()))
for i in range(10):
    if i not in err:                        #고장나지 않은 버튼의 리스트 만들기
        num.append(i)
num.sort()

P = [0]*L                                   #L=len --> L자리수이니 P생성
arr = []                                    #만든 조합을 인수화 하여 저장
def f(i,L):
    global P
    if i == L:
        k = 0
        arr.append(0)
        for j in range(L):
            k +=P[j]*(10**j)                #중복순열로 만든 수를 자릿수에 맞추어 계산
        if k >=10**(L-1):
            arr.append(k)
        return
    else:
        for j in num:
            P[i]=j
            f(i+1,L)
f(0,L)
if L == 1:
    t = 0
    for i in num:
        for j in num:
            t = i*10+j
            if len(str(t)) ==2:             #가장 가까운 수가 2자리 수인 경우를 검토하여 제일 작게 입력되는 2자리 수를 append
                arr.append(t)

    if num ==[]:
            result =abs(100-N)                     #넣을 수 있는게 없는 상태에서 0까지 가는 방법은 100뿐
    else:
        y =100
        for i in num:
            if abs(N-y)>abs(N-i):           #제일 작은 i 값을 y로 입력
                y = i
        result=(abs(N-y)+1)                 #입력(1)+거리
        for i in arr:
            if len(str(i)) ==2:             #2자리 수가

                if abs(i-N)+2 < result:     #2자리수 입력(2) + 거리(i-n) 값이 더 작을 경우
                    result = abs(i-N)+2     #바꿔준다.
else:
    if 0 in num:
        if len(num) ==1:
            if N+1 < abs(100-N):
                result = N+1
            else:
                result=abs(100-N)
        else:
            k = 0
            t = 0
            t = num[1]*(10**L)                      #4자리수 ____ 에서 10000 도 근접인 경우 포함
            arr.append(t)
            for i in range(L - 1):
                k += num[-1] * (10 ** i)
            arr.append(k)
    elif num==[]:
        k=0
        t=0
    else:
        k = 0
        t = 0
        for i in range(L+1):
            t +=num[0]*(10**i)                  #N자리수보다 큰 N+1자리수 중 제일 작은 후
        arr.append(t)
        for i in range(L - 1):
            k += num[-1] * (10 ** i)
        arr.append(k)
    min_a = 10**7                               #일단 젤 큰수
    for i in arr:
        if abs(N-i)==abs(N-min_a):
            if len(str(i)) <len(str(min_a)):
                min_a=i
        if abs(N-i)<abs(N-min_a):               #절대값이 작은 수 선정
            min_a = i
    wid = len(str(min_a))
    if abs(100-N) < wid + abs(N-min_a):           #100에서 위아래 버튼이 적으면 그 숫자를 출력
        result =(abs(100-N))
    else:
        result=(wid+abs(N-min_a))
print(result)