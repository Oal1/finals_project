def for_loops2():
    for a in range(1,10):
        print(a, end = " ")
        for b in range(1,a+1):
            print("*", end = " ")
        print()