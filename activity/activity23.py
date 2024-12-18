def factorial1():
    a = eval(input("Enter a number: "))
    fact = 1
    
    for i in range (a, 0, -1):
        fact *= 1

    print(f"\nThe factorial of {a} is {fact}.")