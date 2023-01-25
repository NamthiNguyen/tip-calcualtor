"""
By: Namthi Nguyen
project : Day 2 Project: Tip Calculator
description: Designing a tip calculator with more modification, such as printing the total bill per person
"""

#Welcome message
print("**** Welcome to Nam's tip calucaltor ****")

# Ask user for their total bill and allow floating number and store it into a variable call customerbill
customer_bill = float(input("What is the total bill? "))

#need to store how many people to divide the bill by
amt_of_people = int(input("how many people are willing to pay? "))

# storing desire tip amount 
desire_tip = float(input("What percentage tip would you like to give? 10, 12 or 18? "))

#Calculations for getting total bill before tax per person
cost_per_person = (customer_bill) / (amt_of_people) 

#Calculations for getting total bill with tac
tip_per_person = (round(cost_per_person * desire_tip /100, 2 ))
total_tip = (round(customer_bill * desire_tip /100, 2 ))

#Calculations for getting total bill per person to pay
total_bill_per_person = (tip_per_person + cost_per_person)

#Display the final message 
print(f"*** Here is the breakdown of the bill *** \n\n * The cost per person = ${cost_per_person }, \n * Total tip per person = ${tip_per_person}, \n * Total bill per person is ${total_bill_per_person}, \n * You will have to pay ${total_tip} in tips")
print("\n**** Thank you for using the calculator!! ****")
