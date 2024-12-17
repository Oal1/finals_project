#code challenge 12 "arrow"

for e in range(4,0,-1):
    for g in range(1,e):
        print(" ",end=" ")
    for f in range(5-e):
        print("*",end=" ")
    for h in range(5-e):
        print("*",end=" ")
    print()
    
for a in range(1,5):
    print(" ",end=" ")
    for b in range(1,3):
        print(" ",end=" ")
    for c in range(1,2):
        print("*",end=" ")
    for d in range(1,0,-1):
        print("*",end=" ")
    print()
