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