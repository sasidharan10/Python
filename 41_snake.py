import random

ls = ["Snake", "Water", "Gun"]


def getdata():
    print("1) Snake")
    print("2) Water")
    print("3) Gun")
    i = int(input("Enter your Choice : "))
    ch = ""
    if i == 1:
        ch = "Snake"
    elif i == 2:
        ch = "Water"
    elif i == 3:
        ch = "Gun"
    else:
        ch = ""
    return ch


def printdata(rn, ch):
    print("Your Choice :", ch)
    print("Comp Choice :", rn)


print("\n---SNAKE---WATER---GUN---\n")
ch = getdata()
t = 10
while(t):
    t -= 1
    rn = random.choice(ls)
    if rn == ch:
        printdata(rn, ch)
        print("GAME TIED!")
    elif rn == "Snake" and ch == "Water":
        printdata(rn, ch)
        print("YOU LOST!")
    elif rn == "Water" and ch == "Gun":
        printdata(rn, ch)
        print("YOU LOST!")
    elif rn == "Gun" and ch == "Snake":
        printdata(rn, ch)
        print("YOU LOST!")
    else:
        printdata(rn, ch)
        print("YOU WON!")
    ch = getdata()
    # if ch=="":
    #     t=0
