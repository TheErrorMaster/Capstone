import random

# dice is random
def randomDice(n):
    ls = []
    for i in range(n):
        ls.append(random.randint(1,6))
    return ls

#check if duplicates
def duplicates(a):
    ls = []
    for x in a:
        if x in ls:
            return True
        else:
            ls.append(x)
    if len(ls) != 6:
        return True
    return False

# if dice is 1,2,3,4,5,6 then its a straight
# check if all numbers are unique
def straight(a):
    score = 0
    if duplicates(a):
        # print("score: 0")
        return score
    else: 
        print("score: 1500")
        score = 1500
        return score

# [1,3,4,6,3]
def found1OR5(a,b):
    score = 0
    once = False 
    for x in a:
        if x == b:
            # print("found: ", b)
            if b == 1 and once == False:
                # print("point: 100")
                once = True
                score = 100
            elif b == 5 and once == False: 
                # print("point: 50")
                score = 50
    return score
        
# input: [1,2,1,3]
# output: [2,1,2,1] 
def listduplicate(a): 
    ls = []
    for x in a:
        b = 0
        for y in a:
            if x == y:
                b = b + 1
        ls.append(b)
    return ls

#a[2,2,3,3,4,4]
#ls[2,2,2,2,2,2]
def pairs(a):
    score = 0
    ls = listduplicate(a)
    b = 0
    for x in ls:
        if x == 2:
            b = b + 1
    if b == 6:
        # print("score: 1500")
        score = 150
        return score
    return score

# a[1,1,1,2,3,5]
# ls[3,3,3,1,1,1]
def find3Kind(a):
    score = 0
    ls = listduplicate(a)
    kind = 0
    for index,x in enumerate(ls):
        # print("x",x, index)
        if x == 3:
            # print(index)
            kind = index
    # print(kind)
    # print(a[kind])
    if kind == 0:
        # score = 0
        return score
    elif a[kind] == 1:
        # print("score: 1000")
        score = 1000
        return score
    elif a[kind]  == 2:
        # print("score: 200")
        score = 200
        return score
    elif a[kind]  == 3:
        # print("score: 300")
        score = 300
        return score
    elif a[kind]  == 4:
        # print("score: 400")
        score = 400
        return score
    elif a[kind]  == 5:
        # print("score: 500")
        score = 500
        return score
    elif a[kind]  == 6:
        # print("score: 600")
        score = 600
        return score
    else:
        # print("score: 0")
        return score

# a[1,1,1,1,3,5]
# ls[4,4,4,4,1,1]
def find4Kind(a):
    score = 0
    ls = listduplicate(a)
    kind = 0
    for index,x in enumerate(ls):
        # print("x",x, index)
        if x == 4:
            kind = index
    # print(kind)
    # print(a[kind])
    if kind == 0:
        # score = 0
        return score
    elif a[kind] == 1:
        # print("score: 2000")
        score = 2000
        return score
    elif a[kind]  == 2:
        # print("score: 400")
        score = 400
        return score
    elif a[kind]  == 3:
        # print("score: 600")
        score = 600
        return score
    elif a[kind]  == 4:
        # print("score: 800")
        score = 800
        return score
    elif a[kind]  == 5:
        # print("score: 1000")
        score = 1000
        return score
    elif a[kind]  == 6:
        # print("score: 1200")
        score = 1200
        return score
    else:
        # print("score: 0")
        return score

# a[1,1,1,1,1,5]
# ls[5,5,5,5,5,1]
def find5Kind(a):
    score = 0
    ls = listduplicate(a)
    kind = 0
    for index,x in enumerate(ls):
        # print("x",x, index)
        if x == 5:
            kind = index
    # print(kind)
    # print(a[kind])
    if kind == 0:
        # score = 0
        return score
    elif a[kind] == 1:
        # print("score: 4000")
        score = 4000
        return score
    elif a[kind]  == 2:
        # print("score: 800")
        score = 800
        return score
    elif a[kind]  == 3:
        # print("score: 1200")
        score = 1200
        return score
    elif a[kind]  == 4:
        # print("score: 1600")
        score = 1600
        return score
    elif a[kind]  == 5:
        # print("score: 2000")
        score = 2000
        return score
    elif a[kind]  == 6:
        # print("score: 2400")
        score = 2400
        return score
    else:
        # print("score: 0")
        return score

# a[1,1,1,1,1,1]
# ls[6,6,6,6,6,6]
def find6Kind(a):
    score = 0
    ls = listduplicate(a)
    if 1 in ls:
        # print("score: 8000")
        score = 8000
        return score
    elif 2 in ls:
        # print("score: 1600")
        score = 1600
        return score
    elif 3 in ls:
        # print("score: 2400")
        score = 2400
        return score
    elif 4 in ls:
        # print("score: 3200")
        score = 3200
        return score
    elif 5 in ls:
        # print("score: 4000")
        score = 4000
        return score
    elif 6 in ls:
        # print("score: 4800")
        score = 4800
        return score
    else:
        # print("no score")
        return score

def ai():
    dice = 6 # we start with 6 dice
    score = 0
    # randice = randomDice(dice)
    randice = [2,2,3,3,4,4]
    while dice >= 3:
        print(randice)
        str8 = straight(randice)
        pa = pairs(randice)
        f6k = find5Kind(randice)
        f5k = find5Kind(randice)
        f4k = find4Kind(randice)
        f3k = find3Kind(randice)
        f1 = found1OR5(randice,1)
        f5 = found1OR5(randice,5)

        if str8 != 0:
            score = score + str8
            print("found a Straight")
            print("score: +", str8)
            randice = randomDice(dice)
            # print("dice: ",dice)
        elif pa != 0:
            score = score + pa
            print("found pairs")
            print("score: +", pa)
            randice = randomDice(dice)
            # print("dice: ",dice)
        elif f6k != 0:
            score = score + f6k
            print("found 6 of a kind")
            print("score: +", f6k)
            randice = randomDice(dice)
            # print("dice: ",dice)
        elif f5k != 0:
            dice = dice - 5
            score = score + f5k
            print("found 5 of a kind")
            print("score: +", f5k)
            randice = randomDice(dice)
            # print("dice: ",dice)
        elif f4k != 0:
            dice = dice - 4
            score = score + f4k
            print("found 4 of a kind")
            print("score: +", f4k)
            randice = randomDice(dice)
            # print("dice: ",dice)
        elif f3k != 0:
            dice = dice - 3
            score = score + f3k
            print("found 3 of a kind")
            print("score: +", f3k)
            randice = randomDice(dice)
            # print("dice: ",dice)
        elif f1 != 0:
            dice = dice - 1
            score = score + f1
            print("found dice 1")
            print("score: +", f1)
            randice = randomDice(dice)
            # print("dice: ",dice)
        elif f5 != 0:
            dice = dice - 1
            score = score + f5
            print("found dice 5")
            print("score: +", f5)
            randice = randomDice(dice)
            # print("dice: ",dice)
        else:
            print("no dice,no score")
            dice = 0
            score = 0
    # print("less than 3")
    return score
print(ai())
