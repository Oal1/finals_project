def pattern():
    #code_challenge1
    print( " \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t       *** \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t      ***** \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t     ******* \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t      ***** \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t       *** \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t* " )

def name_diamond():
    #code_challenge2
    name = input( " What's your name? --> " )

    print( " \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t* \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t       *** \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t      ***** \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t  * Hi, " + name + " * \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t      ***** \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t       *** \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t* " )

def biodata():
    #code_challenge3
    #Input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    place_of_birth = input("Enter your place of birth: ")
    date_of_birth = input("Enter your date of birth (MM/DD/YYYY): ")
    phone_number = int(input("Enter your contact number: ")) 
    email = input("Enter your email: ")
    civil_status = input("Enter your civil status: ")
    citizenship = input("Enter your citizenship: ")
    occupation = input("Enter your occupation: ")
    language_spoken = input("Enter your language spoken: ")
    height = float(input("Enter your height: "))
    weight = float(input("Enter your weight: "))
    fathers_name = input("Enter your father's name: ")
    mothers_name = input("Enter your mother's name: ")

    #Output
    #Bio Data Sentence Format
    print("\nMy name is" , name , 
    ", I am " , age , " years old " , 
    "and I am a" , gender , 
    " born in " , place_of_birth , 
    " on " , date_of_birth, 
    ". My contact number is" , phone_number , 
    "and my email is" , email , 
    ". I am " , civil_status  , 
    "I am " , citizenship , 
    " and I am " , occupation  , 
    ". I speak" , language_spoken , 
    " and I am" , height , " meters tall ", 
    "and weigh" , weight , "kilograms " 
    ". My father's name is" , fathers_name , 
    "and my mother's name is" , mothers_name, ". \n"
    )

    #Bio Data Format
    print( 
    " Bio Data Information "
    " \n ----------------------------- "
    " \n Name: " , name ,
    " \n Age: " , age , 
    " \n Gender: " , gender , 
    " \n Place of birth: " , place_of_birth , 
    " \n Date of birth: " , date_of_birth ,
    " \n Phone number: " , phone_number ,
    " \n Email: " , email , 
    " \n Civil status: " , civil_status ,
    " \n Citizenship: " , citizenship , 
    " \n Occupation: " , occupation ,
    " \n Language spoken: " , language_spoken , 
    " \n Height: " , height , 
    " \n Weight: " , weight ,
    " \n Father's name: " , fathers_name ,
    " \n Mother's name: " , mothers_name ,
    " \n ----------------------------- " 
    )

def arithmetic():
    #code_challenge4
#input
    num1 = eval(input( " Enter a number: " ))

    num2 = eval(input( " Enter another number: " ))

    answer1 = num1 + num2
    answer2 = num1 - num2 
    answer3 = num1 * num2
    answer4 = num1 / num2
    answer5 = num1 ** num2
    answer6 = num1 % num2 
    answer7 = num1 // num2


    #output
    print ( "\n The sum of" , num1 , " and " , num2 , " is " , answer1 )
    print( " The difference of" , num1 , " and " , num2 , " is " , answer2 )
    print( " The product of" , num1 , " and " , num2 , " is " , answer3 )
    print( " The quotient of" , num1 , " and " , num2 , " is " , answer4 )
    print( " The exponent by" , num1 , " and" , num2 , " is " , answer5 )
    print( " The remainder of" , num1 , " and " , num2 , " is " , answer6 )
    print( " The floor division of" , num1 , " and " , num2 , " is " , answer7 )

def temperature():
#code challenge 5
    print("Fahrenheit to Celsius Converter Program")

    print("----------------------------------------")

    fahrenheit = eval(input("Enter temperature: "))

    celsius = ((fahrenheit - 32) * 5 ) / 9

    print(f"{fahrenheit} degrees Fahrenheit converted to Celsius is {round(celsius)} degrees.")

def grading():
    #code challenge 6 
    prelim = eval(input("Enter your prelim grade: "))
    midterm = eval(input("Enter your midterm grade: "))
    semi_final = eval(input("Enter your semi-final grade: "))
    final = eval(input("Enter your final grade: "))
    quiz = eval(input("Enter your quiz grade: "))
    project = eval(input("Enter your project grade: "))


    if prelim > 100 or midterm > 100 or semi_final > 100 or final > 100 or quiz > 100 or project > 100:
        print("\nInvalid grade. Please enter a value between 75 and 100.")
    else:
        
        fg = (prelim * .15) + (midterm * .15) + (semi_final * .15) + (final * .15) + (quiz * .25) + (project * .15)
        print(f"\nFinal grade: {round(fg)}\n")

    
        if fg >= 75 and fg <= 100:
            print(f"Congratulations, you passed the course!")
        else:
            print(f"Sorry, you failed.")

def grocery():
    #code challenge 7
#grocery

    isBuy = input( "Did you buy the grocery? (Yes/No): " )

    if isBuy.lower() == "yes" :
        item = input( "Enter the NAME of the item: " )
        price = float(input( "Enter the PRICE of the item: "))
        age = int(input( "Enter your AGE: " ))
        amount_g= float(input( "Enter the AMOUNT given: " ))
        
    if item.lower() == "pork" :
        print( f"\nName of the item: {item}" )
        print( f"Price of the item: {price} PHP" )
                
    if age >= 1 and age <= 59  :
        tax_price = price * 0.123
        total_price = price + tax_price
        change = amount_g - total_price
        currency_symbol = "PHP"
                
        print( "Not eligible for senior discount." ) 
        print( f"\nHi, customer, you purchased a/an {item} with a price of {price} {currency_symbol} plus 12.3% tax ({tax_price}) {currency_symbol} total of {total_price} {currency_symbol}. " )
        print( f"\nAmount given: {amount_g} {currency_symbol} " )
        print( f"Change: {round(change)} {currency_symbol} " )
        print( f"\nThank you for shopping." )
        
    elif age >= 60 :
        tax_price = price * 0.123
        total_price = price + tax_price
        discount_price = total_price * 0.052
        final_price = total_price - discount_price
        change = amount_g - final_price
        currency_symbol = "PHP"
                
        print( "Eligible for senior discount of 5.2% to the total price." )
        print( f"\nHi, customer, you purchased a/an {item} with a price of {price} {currency_symbol} plus 12.3% tax ({tax_price}) {currency_symbol} total of {total_price} {currency_symbol} with a discount of 5.2% ({discount_price}) {currency_symbol} total of {final_price} {currency_symbol}. " )
        print( f"\nAmount given: {amount_g} {currency_symbol}" )
        print( f"Change: {round(change)} {currency_symbol}" )
        print( f"\nThank you for shopping." )
    else:
        print( "Thank you for visiting." )

def sum_ten():
    #code_challenge8
    sum = 0

    for a in range(10):
        num = eval(input(f"Enter any number #{a +1} : "))
        sum += num
        
    print(f"\nThe sum of 10 random numbers is {sum}. ")

def inv_triange():
    #code_challenge9
    for a in range(10, 0, -1):
        for b in range(10 - a):
            print(" ", end=" ")
        for c in range(0, a): 
            print("*", end=" ")
        print()

def even_diamond():
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

def odd_diamond():
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

def arrow():
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

def number_diamond():
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

def summation():
    #code_challange14
#collect a number
#enter a number
#loop terminated
#the sum of all given number
    isNum = True
    sum = 0 

    while isNum:
        ask = input("Enter a number(or type 'stop' to finish): ")
        
        if ask == "stop":
            isNum = False
            break
        else:
            num = int(ask)
            sum += num
            print(f"The sum of all given number is {sum}.")
            
    print("\nLoop terminated.")
    print(f"The final sum of all given number is {sum}.")

def triangle():
    #code_challenge15
    import os

    isTri = True
    numTri = 0

    while isTri == True:
        ask = input("Do you want to create a new triangle? (Yes/No): ")

        if ask.lower() == "no":
            print("Program/Loop Terminated")
            break
        elif ask.lower() == "yes":
            os.system('clear')
            numTri += 1
            for a in range(1,6):
                for b in range(1,numTri+1):
                    for c in range(1,a+1):
                        print("*",end=" ")
                    for d in range(6,a,-1):
                        print(" ",end=" ")
                print()
            continue
        else:
            os.system('clear')
            print("Invalid answer, please answer yes or no only.")
            continue

def banking():
    account_name = ""
current_balance = 0.0

def deposit(amount):
    global current_balance
    current_balance += amount
    print(f"Successfully deposited: ₱{amount:.2f}. New Balance: ₱{current_balance:.2f}")

def withdraw(amount):
    global current_balance
    if amount > current_balance:
        print("Error: Insufficient funds!")
    else:
        current_balance -= amount
        print(f"Successfully withdrew: ₱{amount:.2f}. New Balance: ₱{current_balance:.2f}")

def check_balance():
    print(f"Current Balance: ₱{current_balance:.2f}")

def breakdown_denomination(amount):
    denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    breakdown = {}
    
    for denom in denominations:
        count = amount // denom
        if count > 0:
            breakdown[denom] = count
            amount -= denom * count

    return breakdown
    
def print_breakdown(breakdown):
    print("Denomination Breakdown:")
    for denom, count in breakdown.items():
        print(f"₱{denom}: {count} piece(s)")

def main():
    global account_name, current_balance
    print("Welcome to the Simple Banking System!")
    
    account_name = input("Enter account holder's name: ")
    initial_deposit = float(input("Enter initial deposit: ₱"))
    current_balance = initial_deposit

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Breakdown Denomination")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: ₱"))
            deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: ₱"))
            withdraw(amount)
        elif choice == '3':
            check_balance()
        elif choice == '4':
            amount = float(input("Enter amount to breakdown: ₱"))
            breakdown = breakdown_denomination(amount)
            print_breakdown(breakdown)
        elif choice == '5':
            print("Thank you for using the Simple Banking System!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()