def biodata():
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
