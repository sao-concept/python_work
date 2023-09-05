answer = 6
user_input = int(input("Guess a number between 1 and 10\n"))

if user_input == answer:
    print("Congratulations, you guess right!")

elif user_input > answer:
    print("Oh! on the high side, guess with lower number")
    user_input = int(input("guess again\n"))
    if user_input == answer:
        print("Congratulations, you guess right!")
    else:
        user_input = int(input("guess again\n"))
        print("Sorry, you guessed wrong")

else:
    print("Your guess is low, try a higher number")
    user_input = int(input("guess again\n"))
    if user_input == answer:
        print("Congratulations, you guess right!")
    else:
        user_input = int(input("guess again\n"))
        print("Sorry, you guessed wrong")
