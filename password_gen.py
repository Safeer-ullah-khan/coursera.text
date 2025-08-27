# import random
# import string

# Inputs= string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
# pasword_len=7
# result=""
# for i in range(pasword_len):
#     result+=(random.choice(Inputs))
# print(result)
'''Random Password by join method'''
# import random
# import string
# Inputs= string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
# passlen=8
# Result="".join([random.choice(Inputs) for i in range(passlen)])
# print(Result)
'''Another join problem'''
Fruits=[]
for i in range(5):
    User=input("Enter a Fruit name ")
    Fruits.append(User)
Result="-".join(Fruits)
print("Fruites are ",Result)


