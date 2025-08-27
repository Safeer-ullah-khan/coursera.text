import random
name=input("Enter Your Name :")
attempts=0
score=0
while True:
    target=random.randint(1,6)
    Guess=int(input("Enter a Number For Guess :"))
    print("The Rolled Number is :",target)
    attempts+=1

    if(Guess==target):
        print("good guess")
        score+=1
    elif(Guess!=target):
         print("wrong Guess")

    ask=input("You want to play again (yes or no)")

    if(ask=="no"):
            print("exit game")
            break
print(f"Player name is {name}")
print(f"Player attempts are {attempts}")
print(f"Player score are {score}")
print(f"Player accuracy  {(score/attempts)*100:.2f}%")
    