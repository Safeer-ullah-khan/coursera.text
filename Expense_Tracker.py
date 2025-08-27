# expenses={}
# while True:
#     ask=input("Enter a category  and amount or (enter exit to quit ):")
#     if(ask=="exit"):
#         print("exit program")
#         break
#     if(ask=="amount"):
#         amount=int(input("Enter a amount"))
#     if(ask=="category"):
#         cata=input("Enter a category").upper()
#         if cata in expenses:
#             expenses[cata]+=amount
#         else:
#             expenses[cata]=amount

# print("Expenses are :")
# for cata, amount in expenses.items():
#     print(f"The expenses are {cata}:{amount}")
# print("Total expenses:", sum(expenses.values()))
expenses={}
while True:
    ask=input("""Enter category and amount to save record:
     Enter summary to watch all records:
     Enter remove for deletion of amount from category:
     and Enter exit to quit program""")
    if(ask.lower()=="exit"):
       print("Quit program")
       break
    if(ask=="summary"):
        print("--Expenses Summary--")
        for category,amount in expenses.items():
            print(f"The expenses are {category}:{amount}")
        print("Total expenses are", sum(expenses.values()))
        continue
    if(ask.lower().startswith("remove")):
        try:
            _,category,amount=ask.split()
            category=category.upper()
            amount=int(amount)
            if category in expenses:
                expenses[category]-=amount
                print("Amount is successfully Removed")
                if expenses[category]<=0:
                    expenses.pop(category)
            else:
                print("category not found")
        except:
            print("Invalid Command")
        continue
    try:
        category,amount=ask.split()
        category=category.upper()
        amount=int(amount)

        if category in expenses:
            expenses[category]+=amount
        else:
            expenses[category]=amount
        print(f"added amount is {category}:{amount}")
    except:
     print("Invalid options and try again")
print("--Expenses Summary--")
for category,amount in expenses.items():
    print(f"The expenses are {category}:{amount}")
print("Total expenses are", sum(expenses.values())) 
print("-"*30)   