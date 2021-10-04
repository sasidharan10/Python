guess = 9

num = 51
print("\n----------NUMBER GAME----------\n")
while(guess):
    guess -= 1
    c = int(input("Enter a Number (1-100) : "))
    if c == num:
        print("YOU WON!!!")
        print("The number is :", num)
        print("Number of guesses :", 9-guess)
        break
    elif c < num:
        print("Your number is smaller!!!")
        print("Try again...")
    else:
        print("Your number is Larger!!!")
        print("Try again...")

if guess == 0:
    print("YOU LOST!!!")
