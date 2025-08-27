vowels=['a','e','i','o','u']
User_input=input("Enter a Sentance!").lower()
count=0
for letters in User_input:
    if letters in vowels:
        count+=1

print("Number of vovels are", count)


