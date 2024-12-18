def triangle():
    num = eval(input("Enter a number of triangle/s: "))

    for a in range(1,5):
        for d in range(1, num + 1):
            for b in range(1, a + 1):
                print("*", end= " ")
            for c in range(5, a, -1):
                print(" ",end= " ")
            print(end=" ")
        print()