def while_name():
    #activity21
    #keep asking name, type 'stop' stop program

    while True:
        name = input("Enter name: ")
        if name.lower() == "stop":
            print("Program Terminated")
            break

