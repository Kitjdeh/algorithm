#이진수 <=> 십진수 변환 함수 생성
#해당 명령어에 맞게 해독하여 실행
#종료조건 발생시 INF넣어서 break


#문자열 이진수를 정수 십진법 변환
def decimal(memorial):
    num = 0
    L = len(memorial)
    for i in range(L):
        x = int(memorial[-i-1])*2**i
        num += x
    return num

# 정수 십진법을 문자열 변환
def binary(num):
    result = ''
    if num >=2**8 or num <0:
        return '00000000'
    for i in range(7,-1,-1):
        temp = num // 2**i
        num = num % 2**i
        result += str(temp)
    return result

def cal(order, memorial,i):
    global adder
    global PC
    # 만들어둔 십진법=>이진법 / 이진법=>십진법을 이용해 명령어에 맞게 처리
    memory_location = decimal(memorial)
    if order == '000':
        arr[memory_location] = adder
    elif order == '001':
        adder = arr[memory_location]
    elif order == '010' and adder == '00000000':
        PC = memory_location
    elif order == '011':
        return
    elif order =='100':
        num = decimal(adder)
        num = (num-1)%256
        # print(num)
        adder = binary(num)
    elif order =='101':
        num = decimal(adder)
        num = (num+1)%256
        adder = binary(num)
    elif order == '110':
        PC = memory_location
    elif order == '111':
        PC = 10000000000

while True:
    try:
        arr = [[0] for _ in range(32)]
        adder = '00000000'
        PC = 0
        for i in range(32):
            arr[i] = input()
        while True:
            # 명령어를 자른다.
            order = arr[PC][:3]
            memorial = arr[PC][3:]

            # 실행전 PC값에 +1을 한다.
            PC = (PC+1)%32

            cal(order, memorial, PC)
            # 종료 조건을 걍 INF넣어서 확인
            if PC == 10000000000:
                break
        print(adder)
    except EOFError:
        break







