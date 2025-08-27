Contacts={"Safeer":"03306829477",
              "Ahmad":"03460967530",
              "Mudassar":"03491912344",
              "Tahir":"03119858321"}
while True:
    def Menu():
        print("---Menu for contacts---")
        print("1.Add contacts")
        print("2.Search contacts")
        print("3.View contacts")
        print("4.Update contact")
        print("5.Exit")
    Menu()
    User=input("Enter your Choice(1-4)")

    if(User=="1"):
        name=input("Enter name")
        Number=input("Enter Number")
        if name in Contacts:
           print("Already Exit")
        else:
            Contacts[name]=Number
            print("Program added successfully")
    elif(User=="2"):
        Name=input("Enter name to search")
        if Name in Contacts:
            print("Contact Info is:",Contacts.get(Name))
        else:
            print("Contact Does not Exist")
    elif(User=="3"):
        for name,Number in Contacts.items():
          print(name,":",Number)
    elif(User=="4"):
        ask=input("Enter a name to update")
        if name in Contacts:
            New_number=input('Enter number to change')
            Contacts[name]=New_number
            print("Number is successfully updated")
        else:
            print("contact not found")
    elif(User=="5"):
        print("Program Exit")
        break
    else:
        print("Wrong option")

