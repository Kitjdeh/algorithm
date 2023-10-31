N = int(input())
for tc in range(1,N+1):
    arr = input()
    a = [0]
    word_list = []
    N = len(arr)
    for i in range(1,N):
        if arr[i] == " ":
            a.append(i)
    a.append(N)
    if len(a)<2:
        print(arr)
    else:
        for j in range(len(a)-1):
            word_list.append(arr[a[j]:a[j+1]])
        rev = word_list[::]
        print(rev)

