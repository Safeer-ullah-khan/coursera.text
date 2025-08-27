# task_list=["task1","task2","task3","task4","task5"]
# def menu_system():
#     while True:
#         print("1:Add Tasks")
#         print("2:Remove Tasks")
#         print("3:View Tasks")
#         print("4:Exit    ")
#         User_Choice=input("Enter a Choice (1-4):")

#         if(User_Choice=="1"):
#             user=input("Enter a Task to append ")
#             task_list.append(user)
#         elif(User_Choice=="2"):
#             user=input("Enter task to Remove")
#             task_list.remove(user)
#         elif(User_Choice=="3"):
#             for index, task in enumerate(task_list,start=1):
#                 print(f"{index}.{task}")
#         elif(User_Choice=="4"):
#             print("exit program")
#             break
#         else:
#             print("Invalid Option")
# menu_system()
task_list=["task1","task2","task3","task4","task5"]
def menu_system():
    while True:
        print("1:Add Tasks")
        print("2:Remove Tasks")
        print("3:View Tasks")
        print("4:Exit    ")
        User_Choice=input("Enter a Choice (1-4):")

        if(User_Choice=="1"):
            user=input("Enter a Task to append ")
            task_list.append(user)
        elif(User_Choice=="2"):
            try:
                user=input("Enter task to Remove")
                task_list.remove(user)
            except ValueError:
                print("---Enter Proper Task---")
        elif(User_Choice=="3"):
            print(task_list)
        elif(User_Choice=="4"):
            print("exit program")
            break
        else:
            print("Invalid Option")
menu_system()
