#1. 좌표값을 오름차순 정리한다.
#2. N개의 센서에는 N-1개의 구간이 있다.
#3. 각 구간을 커버하는 K개의 구역을 만들어야 한다.
#4. 가장 거리가 큰 구간을 기준으로 list들을 잘라간다.
#5. 갯수가 K개가 된다면 합을 구한다.


N = int(input())
K = int(input())
sensor = list(map(int,input().split()))
#1. 좌표값을 오름차순 정리한다.
sensor.sort()
arr = []
#2. N개의 센서에는 N-1개의 구간이 있다.
if K>N:
    print(0)
else:

    for i in range(N-1):
        if sensor[i+1] != sensor[i]:
            arr.append(sensor[i+1]-sensor[i])
    cnt =1
    #3. 각 구간을 커버하는 K개의 구역을 만들어야 한다.
    while cnt != K:
        L = len(arr)
        max = 0
        maxidx = 0
        for i in range(L):
            if arr[i] > max:
                max = arr[i]
                maxidx = i
    # 4. 가장 거리가 큰 구간을 기준으로 list들을 잘라간다.
        arr.pop(maxidx)
        cnt +=1
    result = 0
    for i in range(len(arr)):
        result +=arr[i]
    print(result)

# a = [1, 6, 9, 3, 6, 7]
#  -> [1,3,6,6,7,9]
#  -> [2,3,1,2]