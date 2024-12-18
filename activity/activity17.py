def mul_table():
    #activity17
    #multiplication table
    columns = int(input("Enter mumber of columns: "))
    for b in range(1,columns+1):
        print(f" {b}", end="")
        for a in range(2,columns+1):
            print(f"\t{b * a}",end="")
        print()