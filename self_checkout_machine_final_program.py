inventory = {'bread': 10, 'milk': 12, 'cola': 7, 'fanta': 7,
             'water': 7, 'newspaper': 12, 'magazine': 18, 'candy': 13,
             'juice': 7, 'orange': 3, 'strawberry': 25, 'mango': 99}
#Create a dictionary containing item names and prices

basket = [] #Create an empty list named 'basket'
total = [] #Create an empty list named 'total'

print('Hello there!') #Print this line
def cashier(): #Create a function named 'cashier' with no arguments
    user_answer = input('What would you like to purchase? ').lower()
    #Ask the user to input a product name, change the input to lower case letters
    while user_answer != 'quit': #While the user does not input 'quit', perform the following lines
        if user_answer in inventory:
        #Check if 'user_answer' is in the dictionary 'inventory', if it is, perform the following lines
            basket.append(user_answer)#Add 'user_answer' to the list 'basket'
            user_answer = input('This item has been added to the basket. What else would you like to purchase (Type Quit to end program)? ').lower()
            #Inform the user that their product has been added to the 'basket'.
            #Ask the user if they want to enter another product name
            #Inform the user that they can enter the word 'quit' to finish entering products.
        else:
        #If the user enters a product name which is not in the dictionary named 'inventory', display this line
            user_answer = input('Sorry, we do not have this item. What else would you like to purchase (Type Quit to end program)? ')
            #Display this line and ask the user if they want to enter a new product name.
            
cashier() #Run the function named 'cashier'

print('Here is your shopping basket: ', basket) #Display the user's 'basket'

answer = input('Do you want to add anything else to your shopping basket? (Yes/No)? ').lower()
#Ask the user if they would like to input a new item, assign this value to the variable 'answer'

if answer == 'yes': #If 'answer' equals 'yes', perform the following lines
    cashier() #Run the function named 'cashier'
    print('Here is your final shopping basket: ', basket) #Print this message

for items in basket: #For every item in the list 'basket', perform the following lines'
    total.append(inventory[items]) #Add the corresponding value to the list 'total'

amount_to_pay = sum(total)
#Add the values in the list 'total' together. Store this value in the variable 'amount_to_pay'

currency = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100]
#The types of coins that the user can enter into the self-checkout machine
while amount_to_pay > 0: #While 'amount_to_pay' is bigger than 0, perform the following lines
    amount_to_pay = "{:.2f}".format(amount_to_pay)
    #Format the variable 'amount_to_pay' so that it is a string which contains two numbers after the decimal point
    print('You need to pay £', amount_to_pay) #Print this line
    amount_to_pay = float(amount_to_pay) #Change the variable 'amount_to_pay' back into a float variable
    try: #Try to run the code under this block
        amount_needed_to_pay = float(input('Please pay: '))
        if amount_needed_to_pay in currency: #Check if the input is in the list 'currency'
            amount_needed_to_pay = float(amount_needed_to_pay) #Turn the variable 'amount_needed_to_pay' into a float variable
            amount_to_pay = amount_to_pay - amount_needed_to_pay
            #Perform the calculation 'amount_to_pay = amount_to_pay - amount_needed_to_pay'
        else:
            print('Invalid coin, please try again') #If the user input is not in the list 'currency', print this message
        #Ask the user to enter a float value, store this value in the variable 'amount_needed_to_pay'
        amount_needed_to_pay = "{:.2f}".format(amount_needed_to_pay)
        #Format the variable 'amount_needed_to_pay' so that it is a string which contains two numbers after the decimal point
    except ValueError: #If there is a 'ValueError' when running the code in the try block, run the code under this block
        print('Invalid Input. Only numbers are accepted') #Print this line
        continue #Continue running the loop
    amount_needed_to_pay = float(amount_needed_to_pay) 

amount_to_pay = -(amount_to_pay) #Perform the calculation 'amount_to_pay = -(amount_to_pay)
amount_to_pay = "{:.2f}".format((amount_to_pay))
#Format the variable 'amount_to_pay' so that it is a string which contains two numbers after the decimal point
amount_to_pay = float(amount_to_pay) #Turn the variable 'amount_to_pay' into a float variable
print('\nWe need to return £', amount_to_pay) #Print this line'

change = 0 #Create a variable named 'change' which holds the value '0'

while amount_to_pay >= 2: #While 'amount_to_pay' is less than or equal to '2', perform the following lines of code
    amount_to_pay = amount_to_pay - 2 #Perform the calculation 'amount_to_pay = amount_to_pay - 2'
    change = change + 1 #Perform the calculation 'change = change + 1'

print(change, "£2 coins") #Print this line

change = 0 #Modify the value of the variable 'change'. Set it to '0'

while amount_to_pay >= 1: #While 'amount_to_pay' is less than or equal to '1', perform the following lines of code
    amount_to_pay = amount_to_pay - 1 #Perform the calculation 'amount_to_pay = amount_to_pay - 1'
    change = change + 1 #Perform the calculation 'change = change + 1'
    
print(change, "£1 coins") #Print this line


change = 0 #Modify the value of the variable 'change'. Set it to '0'

while amount_to_pay >= 0.5: #While 'amount_to_pay' is less than or equal to '0.5', perform the following lines of code
    amount_to_pay = amount_to_pay - 0.5 #Perform the calculation 'amount_to_pay = amount_to_pay - 0.5'
    change = change + 1 #Perform the calculation 'change = change + 0.5'

print(change, "50p coins") #Print this line

change = 0 #Modify the value of the variable 'change'. Set it to '0'

while amount_to_pay >= 0.2: #While 'amount_to_pay' is less than or equal to '0.2', perform the following lines of code
    amount_to_pay = amount_to_pay - 0.2 #Perform the calculation 'amount_to_pay = amount_to_pay - 0.2'
    change = change + 1 #Perform the calculation 'change = change + 0.2'

print(change, '20p coins') #Print this line

change = 0 #Modify the value of the variable 'change'. Set it to '0'

while amount_to_pay >= 0.1: #While 'amount_to_pay' is less than or equal to '0.1', perform the following lines of code
    amount_to_pay = amount_to_pay - 0.1 #Perform the calculation 'amount_to_pay = amount_to_pay - 0.1'
    change = change + 1 #Perform the calculation 'change = change + 0.1'

print(change, "10p coins") #Print this line

change = 0 #Modify the value of the variable 'change'. Set it to '0'

while amount_to_pay >= 0.05: #While 'amount_to_pay' is less than or equal to '0.05', perform the following lines of code
    amount_to_pay = amount_to_pay - 0.05 #Perform the calculation 'amount_to_pay = amount_to_pay - 0.05'
    change = change + 1 #Perform the calculation 'change = change + 0.05'

print(change, "5p coins") #Print this line

change = 0 #Modify the value of the variable 'change'. Set it to '0'

while amount_to_pay >= 0.02: #While 'amount_to_pay' is less than or equal to '0.02', perform the following lines of code
    amount_to_pay = amount_to_pay - 0.02 #Perform the calculation 'amount_to_pay = amount_to_pay - 0.02'
    change = change + 1 #Perform the calculation 'change = change + 0.02'
    
print(change, "2p coins") #Print this line

change = 0 #Modify the value of the variable 'change'. Set it to '0'

while amount_to_pay >= 0.01: #While 'amount_to_pay' is less than or equal to '0.01', perform the following lines of code
    amount_to_pay = amount_to_pay - 0.01 #Perform the calculation 'amount_to_pay = amount_to_pay - 0.01'
    change = change + 1 #Perform the calculation 'change = change + 0.01'

print(change, "1p coins") #Print this line

print('\nThank you for shopping at our store') #Print this line
