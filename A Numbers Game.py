import random

# 코드를 작성하세요.
R = random.randint(1, 20)
print(R)

for i in range(1, 5):
    ip = int(input("기회가"+ str(5 - i)+ "번 남았습니다. 1-20 사이의 숫자를 맞혀보세요:"))
    if ip > R:
        print('Down')
    elif ip < R:
        print('UP')
    else:
        print('축하합니다.'+ str(i) +'번만에 숫자를 맞히셨습니다.')
        break

print("아쉽습니다. 정답은 "+str(R)+'입니다.')