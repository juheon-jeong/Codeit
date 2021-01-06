from random import randint

def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1,45)
        if num not in numbers:
            numbers.append(num)

    return numbers

def draw_winning_numbers():
    temp=generate_numbers(7)
    new_list= sorted(temp[:6]) + temp[6:]
    return new_list

def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for i in numbers:
        if i in winning_numbers:
            count +=1
    return count


def check(numbers, winning_numbers):
    cor=count_matching_numbers(numbers, winning_numbers)
    if cor == 6:
        for x in numbers:
            if x == winning_numbers[6]:
                return 50000000
        return 1000000000
    elif cor == 5:
        return 1000000
    elif cor == 4:
        return 50000
    elif cor == 3:
        return 5000
    else:
        return 0
