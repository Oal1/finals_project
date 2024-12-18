import os
import code_challenges

def clear_console():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_console()  # Clear the console at the start of each loop
    print("Welcome to Code Challenge Menu")
    print("1 - code_challenge1 \n2 - code_challenge2 \n3 - code_challenge3 \n4 - code_challenge4 \n5 - code_challenge5 \n6 - code_challenge6 \n7 - code_challenge7 \n8 - code_challenge8 \n9 - code_challenge9 \n10 - code_challenge10 \n11 - code_challenge11 \n12 - code_challenge12 \n13 - code_challenge13 \n14 - code_challenge14 \n15 - code_challenge15 \n16 - code_challenge16")
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and terminate the program

    if user_input == "1":
        code_challenges.pattern()
    elif user_input == "2":
        code_challenges.name_diamond()
    elif user_input == "3":
        code_challenges.biodata()
    elif user_input == "4":
        code_challenges.arithmetic()
    elif user_input == "5":
        code_challenges.temperature()
    elif user_input == "6":
        code_challenges.grading()
    elif user_input == "7":
        code_challenges.grocery()
    elif user_input == "8":
        code_challenges.sum_ten()
    elif user_input == "9":
        code_challenges.inv_triangle()
    elif user_input == "10":
        code_challenges.even_diamond()
    elif user_input == "11":
        code_challenges.odd_diamond()
    elif user_input == "12":
        code_challenges.arrow()
    elif user_input == "13":
        code_challenges.number_diamond()
    elif user_input == "14":
        code_challenges.summation()
    elif user_input == "15":
        code_challenges.triangle()
    elif user_input == "16":
        code_challenges.banking()
    else:
        print("Invalid input. Please enter a number between 1 and 16 or 'exit' to quit.")

    input("Press Enter to continue...")  # Wait for user to press Enter before clearing the console again