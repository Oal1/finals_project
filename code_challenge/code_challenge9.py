for a in range(10, 0, -1):
    for b in range(10 - a):
        print(" ", end=" ")
    for c in range(0, a): 
        print("*", end=" ")
    print()