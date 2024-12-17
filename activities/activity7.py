def miner():
    silver = 1
    miner = input("Hi, what is your name?: ")
    isSilver = input("Is your mineral silver?: ")
    
    if isSilver.lower() == "yes":
        silver += 3
        print(f"Hi, {miner} your total mineral is {silver}")
    else:
        print(f"Hi, {miner} your total mineral is {silver}")