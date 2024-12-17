#code challenge 13 "number diamond"

n = 5

for a in range(1,n+1):
    print("  "*(n-a),end=" ")
    
    for b in range(a,0,-1):
        print(b,end=" ")
        
    for c in range(2,a+1):
        print(c,end=" ")
    print()
    
for a in range(4,0,-1):
    print("  "*(n-a),end=" ")
    
    for b in range(a,0,-1):
        print(b,end=" ")
        
    for c in range(2,a+1):
        print(c,end=" ")
    print()