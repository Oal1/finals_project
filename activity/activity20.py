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

add_triangle()