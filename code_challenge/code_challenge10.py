#code challenge 10 "even diamond"

for e in range(5,0,-1):
    for g in range(1,e):
        print(" ",end=" ")
    for f in range(6-e):
        print("*",end=" ")
    for h in range(6-e):
        print("*",end=" ")
    print()
    
for a in range(1,6):
    for b in range(1,a):
        print(" ",end=" ")
    for c in range(6-a):
        print("*",end=" ")
    for d in range(6-a):
        print("*",end=" ")
    print()
