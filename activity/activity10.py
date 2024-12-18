def enrolled():
    #activity10
    
    name = input("Enter your name: ")

    isStudent = input("Are you currently enrolled in DLL? (Yes/No): ")

    if isStudent.lower() == "yes":
        yearLevel = input("What is your year level: \nF - Freshmen \nS - Sophomore \nJ - Junior \nSr - Senior \nEnter your answer here:")

        if yearLevel.lower() == "f":
            print(f"Hi, {name} you are currently {yearLevel}")
        elif yearLevel.lower() == "s":
            print(f"Hi, {name} you are currently {yearLevel}")
        elif yearLevel.lower() == "j":
            print(f"Hi, {name} you are currently {yearLevel}")
        elif yearLevel.lower() == "sr":
            print(f"Hi, {name} you are currently {yearLevel}")
    else:
        print("Thank you for accessing.")
