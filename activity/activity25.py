def list():
    #activity25
    #list
    #fruit1 = apple
    #fruit2 = banana
    #fruit3 = orange
    #fruit4 = bayabas
    #fruit5 = durian

    fruits = ["apples", "banana", "orange", "bayabas", "durian"]
                #data inside a list is called an 'item'
    print(fruits)

    #access individually item
    print(f"My favorite fruit growing up is {fruits[2]}")
    #add more item to the list
    fruits.append("longgan")
    print(fruits)
    fruits.insert(3,"star-apple")
    print(fruits)

list()