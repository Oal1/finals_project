def password():
    password = input("Enter your password: ")
    if password.lower() == "password" :
        print("Access Granted!")
        print("Enjoy using the system.")
    elif password.lower() == "123" :
        print("Access Granted!")
        print("Enjoy using the system.")
    elif password.lower() == "password123" :
        print("Access Granted!")
        print("Enjoy using the system.")
    else: 
        print("System Exit")

password()