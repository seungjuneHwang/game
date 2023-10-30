import func
# 연산의 달인(연달)
print('연산의 달인(연달) 게임 시작')
# 10문제 반복
for cnt in range(1, 11):
    # 1. 문제만들기
    n1, n2, op = func.munje()
    # 2. 큰값 작은값 자릿수 변경(-, /)
    func.ch_num(n1, n2, op)
    # 3. 유저에게 입력받아서 문제 출력 기능(답도 저장)
    user, dab = func.show_munje(n1, n2, op, cnt)
    # 4. 답 체크
    func.dab_chk(user, dab)
print('연산의 달인(연달) 게임 종료')
