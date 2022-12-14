import random

num = random.sample(range(0,10),k=4)

def getinput(msg):
    usr = [int(i) for i in list(input(msg))]
    return usr

def get_score(usr,num):
    cow=0
    bull=0
    for i in range(0,4):
        if usr[i]==num[i]:
            cow+=1
        elif usr[i] in num:
            bull+=1
    return [cow,bull]

usr = getinput("Guess a four-digit number. ")
trial = 0
while True:
    score = get_score(usr,num)
    if score[0] == 4:
        print("You got it in {z} trials. Well done.".format(z=trial))
        break
    else:
        trial+=1
        print("{x} cows, {y} bulls. (Trial number {z})".format(x=score[0],y=score[1],z=trial))
        usr = getinput("Guess again. ")

