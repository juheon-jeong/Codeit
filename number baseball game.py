from random import randint


def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        rd = randint(0,9)
        if rd not in numbers:
            numbers.append(rd)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.
    while len(new_guess) < 3:
        user = int(input("{}번째 숫자를 입력하세요 ".format((len(new_guess)) + 1)))
        if user > 9 or user < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif user in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(user)
    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(guess)):
        if guess[i] in solution:
            if guess[i] == solution[i]:
                strike_count += 1
            else:
                ball_count += 1

    return strike_count, ball_count
# 여기서부터 게임 시작!
ANSWER = generate_numbers() # 정답 번호 3개를 결정
tries = 0
print(ANSWER)# 몇번만에 맞추었는지를 세는 변수
while True:
    ob = take_guess()       # 사용자 숫자 3개를 결정
    s,b=get_score(ob,ANSWER)
    print("{}S {}B".format(s,b))
    tries += 1
    if s == 3:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
        break