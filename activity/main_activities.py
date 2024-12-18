import activities
import os

def clear_console():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear_console()  # Clear the console at the start of each loop
    print("Welcome to Activity Menu")
    print("2 - activity2 \n3 - activity3 \n4 - activity4 \n5 - activity5 \n6 - activity6 \n7 - activity7 \n8 - activity8 \n9 - activity9 \n10 - activity10 \n11 - activity11 \n12 - activity12 \n13 - activity13 \n14 - activity14 \n15 - activity15 \n16 - activity16 \n17 - activity17 \n18 - activity18 \n19 - activity19 \n20 - activity20 \n21 - activity21")
    user_input = input("Enter a number (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting the program. Goodbye!")
        break  # Exit the loop and terminate the program

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

    else:
        print("Invalid input. Please enter a number between 2 and 21 or 'exit' to quit.")

    input("Press Enter to continue...")  # Wait for user to press Enter before clearing the console again