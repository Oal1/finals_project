#code challenge 7
#grocery

isBuy = input( "Did you buy the grocery? (Yes/No): " )

if isBuy.lower() == "yes" :
    item = input( "Enter the NAME of the item: " )
    price = float(input( "Enter the PRICE of the item: "))
    age = int(input( "Enter your AGE: " ))
    amount_g= float(input( "Enter the AMOUNT given: " ))
    
if item.lower() == "pork" :
	print( f"\nName of the item: {item}" )
	print( f"Price of the item: {price} PHP" )
	 		
if age >= 1 and age <= 59  :
	tax_price = price * 0.123
	total_price = price + tax_price
	change = amount_g - total_price
	currency_symbol = "PHP"
	 	 	 
	print( "Not eligible for senior discount." ) 
	print( f"\nHi, customer, you purchased a/an {item} with a price of {price} {currency_symbol} plus 12.3% tax ({tax_price}) {currency_symbol} total of {total_price} {currency_symbol}. " )
	print( f"\nAmount given: {amount_g} {currency_symbol} " )
	print( f"Change: {round(change)} {currency_symbol} " )
	print( f"\nThank you for shopping." )
	
elif age >= 60 :
    tax_price = price * 0.123
    total_price = price + tax_price
    discount_price = total_price * 0.052
    final_price = total_price - discount_price
    change = amount_g - final_price
    currency_symbol = "PHP"
	 	 	 
    print( "Eligible for senior discount of 5.2% to the total price." )
    print( f"\nHi, customer, you purchased a/an {item} with a price of {price} {currency_symbol} plus 12.3% tax ({tax_price}) {currency_symbol} total of {total_price} {currency_symbol} with a discount of 5.2% ({discount_price}) {currency_symbol} total of {final_price} {currency_symbol}. " )
    print( f"\nAmount given: {amount_g} {currency_symbol}" )
    print( f"Change: {round(change)} {currency_symbol}" )
    print( f"\nThank you for shopping." )
else:
    print( "Thank you for visiting." )