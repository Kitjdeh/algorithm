t = int(input())
arr=[[0,0]]
for i in range(6):
    m = arr[-1]                     #이동하려는 최신 좌표를 수령
    a,b = map(int,input().split())
    wid = 0
    hei = 0
    if a ==4:                       #1,2,3,4 각방향으로 m값 수정
        m[1] += b
    elif a==3:
        m[1] += -b
    elif a==2:
        m[0] += -b
    elif a==1:
        m[0] += b

    arr.append(m[0:2])              #깊은복사 방지
arr.pop()                           #중복[0,0]제거
wid=[]
hei=[]
for i in range(len(arr)):
    wid.append(arr[i][0])           #x축 값들만 수집
    hei.append(arr[i][1])           #y축 값들만 수집
wid_max = max(wid)                  #육각형의 가장 오른쪽 x좌표
wid_min = min(wid)                  #육각형의 가장 왼쪽 x좌표
a = [wid_max,wid_min]               #x좌표 리스트화
hei_max = max(hei)                  #육각형의 가장 위쪽 y좌표
hei_min = min(hei)                  #육각형의 가장 아랫족 y좌표
b = [hei_max,hei_min]               #y좌표 리스트화
rec=[]
for i in a:
    for j in b:
        rec.append([i,j])           #큰 직사각형에서 직사각형을 자른게 지금의 육각형이라 가정하여 큰 직사각형의 모서리값 설정
for i in range(4):
    if rec[i] in arr:               #모서리4개중 1개만 없는 육각형이니 1개를 찾음
        pass
    else:
        edg = rec[i]
for i in range(len(arr)):
    if arr[i][0] in a or arr[i][1] in b:    #6각형중 문제의 가운데는 최대,최소값 둘다 없음
        pass
    else:
        cen = arr[i]
S = abs(wid_max-wid_min) * abs(hei_max-hei_min) #전체 큰 직사각형 넓이
L = abs(cen[0]-edg[0])*abs(cen[1]-edg[1])       #잘려진 작은 직사각형 넓이

num = S-L
print(cen)
print(num*t)