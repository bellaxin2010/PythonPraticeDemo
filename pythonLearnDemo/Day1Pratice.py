import random

num = random.randint(0,10)


count =0
while count <5:
    user_guess = int(input("pls input value: "))
    if user_guess == '':
        print("input value pls")
    elif user_guess > num:
        print("larger ")
    elif user_guess < num:
        print("smaller")
    else:
        print("collect")
        break
    count+=1