import os
from code_challenge import code_challenges
from activity import activities

def clear_console():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_console()  # Clear the console at the start of each loop
    print("Welcome to the Main Menu")
    print("1 - Code Challenges")
    print("2 - Activities")
    print("Type 'exit' to quit the program.")
    
    main_choice = input("Please choose an option: ")

    if main_choice.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and terminate the program

    if main_choice == "1":
        # Code Challenges Menu
        while True:
            clear_console()  # Clear the console for the Code Challenges menu
            print("Welcome to Code Challenge Menu")
            print("1 - code_challenge1 \n2 - code_challenge2 \n3 - code_challenge3 \n4 - code_challenge4 \n5 - code_challenge5 \n6 - code_challenge6 \n7 - code_challenge7 \n8 - code_challenge8 \n9 - code_challenge9 \n10 - code_challenge10 \n11 - code_challenge11 \n12 - code_challenge12 \n13 - code_challenge13 \n14 - code_challenge14 \n15 - code_challenge15 \n16 - code_challenge16")
            user_input = input("Enter a number (or type 'back' to return to the main menu): ")

            if user_input.lower() == "back":
                break  # Go back to the main menu

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
                print("Invalid input. Please enter a number between 1 and 16 or 'back' to return.")

            input("Press Enter to continue...")  # Wait for user to press Enter before clearing the console again

    elif main_choice == "2":
        # Activities Menu
        while True:
            clear_console()  # Clear the console for the Activities menu
            print("Welcome to Activity Menu")
            print("2 - activity2 \n3 - activity3 \n4 - activity4 \n5 - activity5 \n6 - activity6 \n7 - activity7 \n8 - activity8 \n9 - activity9 \n10 - activity10 \n11 - activity11 \n12 - activity12 \n13 - activity13 \n14 - activity14 \n15 - activity15 \n16 - activity16 \n17 - activity17 \n18 - activity18 \n19 - activity19 \n20 - activity20 \n21 - activity21")
            user_input = input("Enter a number (or type 'back' to return to the main menu): ")

            if user_input.lower() == "back":
                break  # Go back to the main menu

            if user_input == "2":
                activities.basic_ope()
            elif user_input == "3":
                activities.intro_input()
            elif user_input == "4":
                activities.ari_ope()
            elif user_input == "5":
                activities.temp_conv()
            elif user_input == "6":
                activities.add_update()
            elif user_input == "7":
                activities.miner()
            elif user_input == "8":
                activities.password()
            elif user_input == "9":
                activities.age()
            elif user_input == "10":
                activities.enrolled()
            elif user_input == "11":
                activities.for_loops()
            elif user_input == "12":
                activities.dec_loops()
            elif user_input == "13":
                activities.factorial()
            elif user_input == "14":
                activities.for_loops1()
            elif user_input == "15":
                activities.for_loops2()
            elif user_input == "16":
                activities.half_diamond()
            elif user_input == "17":
                activities.mul_table()
            elif user_input == "18":
                activities.triangle()
            elif user_input == "19":
                activities.name()
            elif user_input == "20":
                activities.add_triangle()
            elif user_input == "21":
                activities.while_name()
