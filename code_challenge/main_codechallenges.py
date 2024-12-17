from code_challenge import code_challenges

while True:
    print("Welcome to Code Challenge Menu")
    print("1 - code_challenge1 \n2 - code_challenge2 \n3 - code_challenge3 \n4 - code_challenge4 \n5 - code_challenge5 \n6 - code_challenge6 \n7 - code_challenge7 \n8 - code_challenge8 \n9 - code_challenge9 \n10 - code_challenge10 \n11 - code_challenge11 \n12 - code_challenge12 \n13 - code_challenge13 \n14 - code_challenge14 \n15 - code_challenge15 \n16 - code_challenge16")
    user_input = input("Enter a number: ")

    if user_input == "1":
        code_challenges.pattern()
    if user_input == "2":
        code_challenges.name_diamond()
    if user_input == "3":
        code_challenges.biodata()
    if user_input == "4":
        code_challenges.arithmetic()
    if user_input == "5":
        code_challenges.temperature()
    if user_input == "6":
        code_challenges.grading()
    if user_input == "7":
        code_challenges.grocery()
    if user_input == "8":
        code_challenges.sum_ten()
    if user_input == "9":
        code_challenges.inv_triange()
    if user_input == "10":
        code_challenges.even_diamond()
    if user_input == "11":
        code_challenges.odd_diamond()
    if user_input == "12":
        code_challenges.arrow()
    if user_input == "13":
        code_challenges.number_diamond()
    if user_input == "14":
        code_challenges.summation()
    if user_input == "15":
        code_challenges.triangle()
    if user_input == "16":
        code_challenges.banking()