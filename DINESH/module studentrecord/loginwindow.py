def login_window():
    username = "abc123"
    password = "abc@123"
    while True:
        user = input("Enter the username: ")
        passwd = input("Enter the password : ")
        if user == username and passwd == password:
            print("Successfully login")
            break
        else:
            print("Invalid ID or password! Please try again.")