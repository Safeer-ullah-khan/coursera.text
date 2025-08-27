# import random
    
# def Dice_roller():
#     Target=random.randint(1,6)
#     print("roll a Dice between (1-6)")
#     print("The rolled number is",Target)
#     return Target
# def sum_total(curr_total,new_roll):
#     return curr_total+new_roll
# atempts=0
# max_attempts=5
# total_sum=0
# while True:  
#      roll=Dice_roller()
#      total_sum=sum_total(total_sum,roll)
#      atempts+=1
#      print(f"The total sum of Rolled Dices is {total_sum}")
#      print(f"The total Number of attempts is {atempts}")

#      ask_again=input("you want to play again: (yes or no)").lower().strip() 

#      if(ask_again=="no"):
#         print("exit game ")
#         break
# print("Thanks for playing")
# print(f"The total sum of Rolled dices is {total_sum}")
# print(f"The total sum  of attempts is {atempts}")
import random
attempts=0
while True:
    Target=random.randint(1,6)
    print("The option in Dices is (1-6)")
    print("the Dice number is ",Target)
    attempts+=1
    if(Target==6):
        print(f"{attempts} attempts is to get {Target}")
        break
    ask=input("Want to roll dice again (yes or no)").lower().strip()
    if(ask=="no"):
        print("game over ")
        break
print("Thanks for playing")
print(f"The total attempts are {attempts}")

    
    




