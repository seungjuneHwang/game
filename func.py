import random
# 함수 정의
def add(a, b):
    print('hello world')
    print(a + b)

# 문제만들기
def munje():
    # 두자리 수가 랜덤으로 하나
    n1 = random.randrange(1, 100)
    # 두자리 수가 랜덤으로 둘
    n2 = random.randrange(1, 10)
    # +, -, *, / 중에 하나
    op_list = ['+', '-', '*', '/']
    op = random.choice(op_list)
    # print(n1, op, n2) # 테스트 출력
    return n1, n2, op

# 큰값 작은값 자릿수 변경(-, /)
def ch_num(n1, n2, op):
    # 만약에 -, / 에서 n1 이 n2 보다 작으면 앞뒤로 바꿈
    if op == '-' or op == '/':
        # print('두수 바꿈')
        # 두수 바꿈 만들어 보세요
        # 큰값 저장기능
        front = max(n1, n2)
        # 작은값 저장기능
        back = min(n1, n2)
        # 두수를 변경
        n1 = front
        n2 = back

# 유저에게 입력받아서 문제 출력 기능(답도 저장)
def show_munje(n1, n2, op, cnt):
    if op == '+':
        dab = n1 + n2
    elif op == '-':
        dab = n1 - n2
    elif op == '*':
        dab = n1 * n2
    elif op == '/':
        dab = n1 / n2

    # 사용자에게 문제 보여주고 사용자가 입력할 수 있게 하고 
    user = int(input(f'{cnt}문제: {n1} {op} {n2} = ' ))
    return user, dab

# 답 체크
def dab_chk(user, dab):
    # 문제의 정답을 맞추면
    if user == dab:
        print('정답 계속')
    else:
        print('땡~')

# add(1, 2)  # 함수 호출
# munje()