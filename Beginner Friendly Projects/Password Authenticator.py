import maskpass

#Create a dictionary containing Usernames(key) & Passwords(values).

database = {
    "Amiram1544" : "15441544",
    "Zahrash1544" : "z15441544",
    "usernamee" : "password"
}


#Keep asking untill the correct username and password is entred 
while True:
    print("*****---LOGIN---******")
    print()
    username = input("Enter your Username: ")


#make a loop

    if username in database:
        while True:
            password = maskpass.advpass("Enter your Password: ") #hide the password using the maskpass module
            print("*****-----------******")

            if password == database[username]:
                print(f"Welcome")
                exit()


    else:
        print("Erorr 404: Username not found")
    








