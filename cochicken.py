with open('data/chicken.txt', 'r', encoding='UTF-8') as f:
    hop = []
    amount = 0
    for line in f:
        day, money = line.strip().split(': ')
        hop.append(money)
    for i in hop:
        amount += int(i)

    print(amount / len(hop))