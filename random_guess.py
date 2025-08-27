import random

computer=random.randint(1, 50)
attempts=0
max_attempts=6
while(attempts<max_attempts):
    Numbers=int(input("Enter a Number"))
    attempts+=1
    if(Numbers==computer):
        print("---Exelent Guess--- :")
        break
    elif(Numbers>computer and Numbers<50):
        print("----Your guess is High----")
    elif(Numbers<computer and Numbers>0):
        print("----Your guess is low----")
    else:
        print("Incorrect options")
if(attempts==max_attempts and Numbers!=computer):
    print("Game over: Please Try again")