# Basic Tip Calculator. 
# Write a program that
#      a) asks for the total bill amount
#      b) asks for the tip percentage. 
#      c) calculates and displays:
#           1 ) the tip amount
#           2)  the total bill including the tip.
# Advanced: 
#      d) asks for a name and dollar amounts of dishes comma separated
#      e) print the total amount owed with name on it.

# Author: Kamila Kalchakeeva
# https://github.com/kkalchake

def main():
 ### Get user inputs
 bill_amount = float(input(('\nWhat is the bill amount? ')))
 tip_percentage = float(input(('What is the tip percentage you wish to add? ')))

### Calculate and output total bill
 tip_amount = (bill_amount * tip_percentage / 100)
 total_bill = bill_amount + tip_amount
 print (f'\n Bill breakdown: ')
 print (f'\n Bill Amount: ${bill_amount} \n Tip: ${tip_amount:.2f}\n\n The total bill with {tip_percentage}% tip is ${total_bill:.2f}\n')

if __name__ == '__main__':
   main()

### Advancements in progress
### Get the user inputs
# number_of_people = int(input('How many people are splitting the check?'))
# in range of number_of_people:
#     name = input('What is your name?')
#     ordered_for = list(input('Enter coma separated format dollar amounts for each dish you ordered))
# takes bill_amount -> calculates all people's order total and assigns tax_amount
# splits tax_amount + tip_amount
# adds above to sum of each dish ordered
### Output whole math
# Output table with each name and how much each owe
# Output confirmation of right math