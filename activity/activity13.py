def factorial():
    a = eval(input("Enter a number: "))
    fact = 1
    
    for i in range (a, 0, -1):
        fact *= i

    print(f"\nThe factorial of {a} is {fact}.")

factorial()