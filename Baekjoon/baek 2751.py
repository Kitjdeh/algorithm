N = int(input())
arr = ['']*2000001
for i in range(N):
    n = int(input())
    arr[n+1000000] = n

for i in arr:
    if i != '':
        print(i)
