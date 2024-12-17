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
