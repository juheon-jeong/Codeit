import random

with open('vocabulary.txt','r', encoding = 'UTF-8') as f:
    lines = f.readlines()

    voca = []
    mean = []

    for line in lines:
        data = line.strip().split(": ")
        voca.append(data[0])   # data[0] == voca
        mean.append(data[1])   # data[1] == mean
    dictionary = dict(zip(mean,voca))


    while True:
        k = random.choice(list(dictionary.keys()))
        answer = input("{}: ".format(k))
        if answer == dictionary[k]:
            print("맞았습니다!\n")
        elif answer =='q':
            break
        else:
            print("틀렸습니다. 정답은 {}입니다.\n".format(dictionary[k]))










