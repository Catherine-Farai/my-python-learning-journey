price = 50 #using if condition
if price < 100:
    print('price is less than 100')

#using multiple print on a if condition
price = 50
quantity = 5
if price*quantity < 500 :
    print('price*quantity is less than 100')
    print('price =', price)
    print('quantity =', quantity)

#using different indent of print on a if condition
price = 5
quantity = 5
if price*quantity < 100:
    print('price less than 500')
    print('price = ', price)
    print('quantity = ', quantity)
print('no if block executed')

#usimg multiple if condition
price = 100

if price > 100:
    print('price is greater than 100')
if price ==100:
    print('price is 100')
if price < 100:
    print('price is less than 100')

#using if, elif and else condition
price = 100

if price > 100:
    print('price is greater than 100')
elif price ==100:
    print('price is 100')
else :
    print('price is less than 100')

price = 50

if price > 100:
    print('price is greater than 100')
elif price ==100:
    print('price is 100')
else :
    print('price is less than 100')

price = 50
quantity = 5
amount = price*quantity

if amount > 100:
    if amount > 500:
        print('amount is greater than 500')
    else:
        if amount< 500 and amount> 400:
            print('amount is ')
        elif amount < 500 and amount > 300:
             print('amount is between 300 and 500')
        else:
             print('amount is between 200 and 500')
elif amount == 100:
    print('amount is 100')
else:
    print('amount is less than 100')
             
    
