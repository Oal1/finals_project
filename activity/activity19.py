def name():
    #activiy19
    #ask name for 5 types, if type 'stop' terminate program

    for a in range(1,6):
        name = input("Enter your name: ")
        if name.lower() == "stop":
            print("Program terminated.")
            break
        else:
            print(f"Hello, {name}")
