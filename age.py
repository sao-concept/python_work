# Program to test if...conditional statement on age
age = eval(input("Enter child's age:\n"))

if age >= 6 and age <= 17:
    print(f"Since your Ward is {age} years old, he/she should be"
          " in grade 1 through 12")
elif age > 17 and age < 25:
    print(f"Your Ward is {age} years old, should be in college")
else:
    print(f"Your Ward is either underage or out of college")
