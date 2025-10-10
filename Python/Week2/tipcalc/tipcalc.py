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

# Need to split the bill? Visit https://kkalchake.github.io/fair_tip_calc/ for advanced calculations

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

