
def half_diamond():

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
    #triangle will be created based on the user input
    num = eval(input("Enter a number of triangle/s: "))

    for a in range(1,5):
        for d in range(1, num + 1):
            for b in range(1, a + 1):
                print("*", end= " ")
            for c in range(5, a, -1):
                print(" ",end= " ")
            print(end=" ")
        print()
        
user = " "
while True:
    if user.lower()== "no":
        break
    choose = input("Choose activity you want to enter: \n1 = Activity 16 \n2 = Activity 17\n3 = Activity 18\n: ")
    if choose.lower() == "1":
        half_diamond()
    elif choose.lower() == "2":
        mul_table()
    elif choose.lower() == "3":
        triangle()
    else:
        print("Invalid input!")
        continue
    print()
    while True:
        tryAgain = input(" Do you want to try to open another activity? (Yes/No) \n: ")
        if tryAgain.lower() == "yes":
            break
        elif tryAgain.lower() == "no":
            break
        else:
            print("Invalid input")
            continue
