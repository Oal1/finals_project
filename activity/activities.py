def basic_ope():
    #activiy2
    num1 = 3 + 2
    num2 = 5 - 4
    # Basic Operations
    print(f"3 + 2 is {num1} \n5 - 4 is {num2}")
    
def intro_input():
    #activity3
    #intro to input
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    sex = input("What is your sex? (M/F): ")
    email = input("Enter your email: ")
    nationality = input("Enter your nationality: ")
    occupation = input("Enter your occupation: ")
    print("\nWelcome",name,", your age is",age,", and your sex is",sex,", and your email is",email,", and your nationality is",nationality,", and your occupation",occupation,".")

def ari_ope():
    #activity4
    #arithmetic operators
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter an another number: "))
    print(f"The sum of {num1} + {num1} is {num1 + num2}")   

def temp_conv():
    #activity 5
    print("Fahrenheit to Celsius Converter Program")
    print("----------------------------------------")
    fahrenheit = eval(input("Enter temperature: "))
    celsius = ((fahrenheit - 32) * 5 ) / 9
    print(f"{fahrenheit} degrees Fahrenheit converted to Celsius is {round(celsius)} degrees.")

def add_update():
    #activity6
    #assignment operators
    x = 5
    print(x)
    x += 5
    print(x)
    x += 10
    print(x)
    x += 15
    print(x)

def miner():
    #activity7
    #asking the miner 
    silver = 1
    miner = input("Hi, what is your name?: ")
    isSilver = input("Is your mineral silver?: ")
    if isSilver.lower() == "yes":
        silver += 3
        print(f"Hi, {miner} your total mineral is {silver}")
    else:
        print(f"Hi, {miner} your total mineral is {silver}")

def password():
    #activity8
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

def age():
    #activity9
    #age
    age = eval(input("Enter your age: "))
    if age >= 1 and age <7 :
        print("Toddler")

def enrolled():
    #activity10
    name = input("Enter your name: ")
    isStudent = input("Are you currently enrolled in DLL? (Yes/No): ")
    if isStudent.lower() == "yes":
        yearLevel = input("What is your year level: \nF - Freshmen \nS - Sophomore \nJ - Junior \nSr - Senior \nEnter your answer here:")
        if yearLevel.lower() == "f":
            f = "Freshmen"
            print(f"Hi, {name} you are currently {f}")
        elif yearLevel.lower() == "s":
            s = "Sophomore"
            print(f"Hi, {name} you are currently {s}")
        elif yearLevel.lower() == "j":
            j = "Junior"
            print(f"Hi, {name} you are currently {j}")
        elif yearLevel.lower() == "sr":
            sr = "Senior"
            print(f"Hi, {name} you are currently {sr}")
    else:
        print("Thank you for accessing.")

def for_loops():
    #activity11
    #nested for loops
    for a in range(1,11):
        print("Hello")
        isPogi = input("Pogi ba? (T/F): ")
        if isPogi.lower() == "t":
            print("True ba?")
        else:
            print("True")
            break

def dec_loops():
    #activity12
    #decrement loops
    for a in range(10, 0 , -1):
        print(a)

def factorial():
    #activity13
    #factorial
    a = eval(input("Enter a number: "))
    fact = 1
    for i in range (a, 0, -1):
        fact *= i
    print(f"\nThe factorial of {a} is {fact}.")

def for_loops1():
    #activity14
    for a in range(1,11):
        print(a, end=" ")
        for b in range(1,11):
            print("*", end= " ")
        print()

def for_loops2():
    #activity15
    for a in range(1,10):
        print(a, end = " ")
        for b in range(1,a+1):
            print("*", end = " ")
        print()

def half_diamond():
    #activity16
    #Upper part of the half-diamond
    for e in range(1,6):
        for d in range(5 - e):
            print(" ",end=" ")
        for f in range(1,e+1):
            print("*",end=" ")
        print()

    #Lower part of the half-diamond
    for a in range(4,0,-1):
        for b in range(5 - a):
            print(" ", end=" ")
        for c in range(1,a+1):
            print("*",end=" ")
        print()

def mul_table():
    #activity17
    #multiplication table
    columns = int(input("Enter mumber of columns: "))
    for b in range(1,columns+1):
        print(f" {b}", end="")
        for a in range(2,columns+1):
            print(f"\t{b * a}",end="")
        print()

def triangle():
    #activity18
    num = eval(input("Enter a number of triangle/s: "))
    for a in range(1,5):
        for d in range(1, num + 1):
            for b in range(1, a + 1):
                print("*", end= " ")
            for c in range(5, a, -1):
                print(" ",end= " ")
            print(end=" ")
        print()

def name():
    #activiy19
    #ask name for 5 types, if type 'stop' terminate program

    for a in range(1,6):
        name = input("Enter your name: ")
        if name.lower() == "stop":
            print("Program terminated.")
            break
        else:
            print(f"Hello, {name}")

def add_triangle():    
    #activity20
    #add triangle if 'yes', and 'no' program terminated
    
    noTri = 1

    def printTriangle(add):
        for a in range(1, 6):
            for b in range(1, add + 1):
                print("* " * a, end="  " * (6 - a))
            print()
    printTriangle(noTri)

    while True:
        ask = input(" Do you wish to continue print triangle? ( yes / no ) ---> ")
        if ask.lower() == "no":
            print("Program/Loop terminated")
            break
        elif ask.lower() == "yes":
            noTri += 1
            printTriangle(noTri)
        else:
            print("Invalid input, try again\n")
            continue

def while_name():
    #activity21
    #keep asking name, type 'stop' stop program

    while True:
        name = input("Enter name: ")
        if name.lower() == "stop":
            print("Program Terminated")
            break

