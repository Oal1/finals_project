#code challenge 11 "odd diamond"

for e in range(1,6):
    for f in range(6-e):
        print(" ",end=" ")
    for g in range(1,e-1):
        print("*",end=" ")
    for h in range(1,e):
        print("*",end=" ")
    print()
    
for a in range(5,0,-1):
    for b in range(5-a):
        print(" ",end=" ")
    for c in range(1,a+1):
        print("*",end=" ")
    for d in range(1,a):
        print("*",end=" ")
    print()