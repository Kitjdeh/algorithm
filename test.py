def main():
    N = 10
    M = 3
    arr =[i for i in range(N)]
    for i in range(N):
        arr[i] = [j*i for j in range(N)]

    N = 10
    M = 3
    result = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            A = [sum(arr[t][j:j+M]) for t in range(i,i+M)]
            B = sum(A)
            if B > result:
                result = B
    print(B)
# main()
if __name__ == "__main__":
	main()
 