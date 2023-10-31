# 1.두 문장 중 짧은 쪽과 긴쪽을 선별
# 2.작은 블록 양옆에 긴 블럭의 길이만큼의 0을 넣어 겁나 긴 블럭 형성
# 3. 겁나 긴 블럭을 긴쪽 블럭길이L만큼 자르면서 중복체크
# 4. 가장 중복이 긴 값을 구함


#같은 길이 a,b의 가장 큰 중복값 찾는 함수
def f(a,b):
    global max_length
    global L
    max_V =0
    result = 0
    for i in range(L):
        if a[i] ==b[i]:
            result +=1
            if max_V < result:
                max_V=result
        else:
            result = 0
    if max_length < max_V:
        max_length = max_V
    return

str1 = input()
str2 = input()

a = len(str1)
b = len(str2)
max_length =0
if a < b:
    center_str = str2
    long_stick = '0'*b+str1+'0'*b
    L = b
else:
    center_str = str1
    long_stick = '0'* a + str2 + '0' * a
    L = a

for i in range(1,1+a+b):
    stack = long_stick[i:i+L]
    f(stack,center_str)

print(max_length)