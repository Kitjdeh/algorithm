N = int(input())
arr = list(map(int,input().split()))
max_i= -1000000
min_i= 1000000
for i in arr:
    if i >= max_i:
        max_i = i
    if i <= min_i:
        min_i = i
print(min_i, max_i)
