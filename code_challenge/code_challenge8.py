def sum_ten():
    sum = 0

    for a in range(10):
        num = eval(input(f"Enter any number #{a +1} : "))
        sum += num
        
    print(f"\nThe sum of 10 random numbers is {sum}. ")