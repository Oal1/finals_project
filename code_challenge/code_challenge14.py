#collect a number
#enter a number
#loop terminated
#the sum of all given number
isNum = True
sum = 0 

while isNum:
    ask = input("Enter a number(or type 'stop' to finish): ")
    
    if ask == "stop":
        isNum = False
        break
    else:
        num = int(ask)
        sum += num
        print(f"The sum of all given number is {sum}.")
        
print("\nLoop terminated.")
print(f"The final sum of all given number is {sum}.")
