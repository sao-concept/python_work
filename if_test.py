my_name = input("Please, enter your name\n")
age = int(input("Enter your age\n"))
print("Hey {0}, your age is {1}".format(my_name.title(), age))

if age >= 30:
    print("You are {0} already, old enough to settle down".format(age))
elif age <= 18:
    print("Hey champ, you are still {0}, you should focus on your study".format(age))
else:
    print("This is the best time to hustle hard, {0}".format(my_name))
