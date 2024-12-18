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
