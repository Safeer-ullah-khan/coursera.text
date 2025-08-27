import random
computer=random.choice([1,2,3])
user_choice=input("enter a choice")
user_dict={"Rock 🥌":1,
              "paper🧻":2,
              "Scissor✂️":3}
Reverse_dict={1:"Rock",
          2:"paper",
          3:"Scissor"}
user=user_dict[user_choice]
print(f"User_choice is {Reverse_dict[user]}\n and computer choice is {Reverse_dict[computer]}")

if(computer==user):
    print("match draw")
elif(computer==1 and user==2):
    print("you lose")
elif(computer==2 and user==3):
    print("you win")
elif(computer==3 and user==1):
    print("you win")
elif(computer==1 and user==3):
    print("you lose")
elif(computer==3 and user==2):
    print("you lose")
elif(computer==2 and user==1):
    print("you win")
else:
    print("Invalid choice")


