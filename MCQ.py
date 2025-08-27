Questions=[{"question":"What is the capital of Pakistan",
            "Options":["A.Dehli","B.Paris","C.Islamabad","D.London"],
            "Answer":"C"},
            {"question":"How ha alphabet in English",
             "Options":["A.23","B.21","C.29""D.26",],
             "Answer":"D"}]
score=0
for q in Questions:
    print(q["question"])
    for option in q["Options"]:
        print(option)
    user=input("Enter Choices A/B/C/D :").upper()
    if(user==q["Answer"]):
        print("Welldone")
        score+=1
    else:
        print("Wrong option")
print(f"The Total Score is {score}")
# Questions=[{"question":"What is the capital of Pakistan",
#             "Options":"A.Dehli B.Paris C.Islamabad D.London",
#             "Answer":"C"},
#             {"question":"How ha alphabet in English",
#              "Options":"A.23 B.21 C.29 D.26",
#              "Answer":"D"}]
# score=0
# for q in Questions:
#     print(q["question"])
#     for Option in q["Options"]:
#         print(Option)
#     user=input("Enter Choices A/B/C/D :").upper()
#     if(user==q["Answer"]):
#         print("Welldone")
#         score+=1
#     else:
#         print("Wrong option")
# print(f"The Total Score is {score}")
# Questions=[{"question":"What is the capital of Pakistan",
#             "Options":"A.Dehli B.Paris C.Islamabad D.London",
#             "Answer":"C"},
#             {"question":"How ha alphabet in English",
#              "Options":"A.23 B.21 C.29 D.26",
#              "Answer":"D"}]
# score=0
# for q in Questions:
#     print(q["question"])
#     for o in Questions:
#         print(q["Options"])
#     user=input("Enter Choices A/B/C/D :").upper()
#     if(user==q["Answer"]):
#         print("Welldone")
#         score+=1
#     else:
#         print("Wrong option")
# print(f"The Total Score is {score}")
