#===========================================================
#
#  Title:       <Pays and Taxes>
#  Course:      CPS 120
#  Homework:    <One>
#  Author:      <Matthew Hernandez>
#  Date:        <1/15/2021>
#  Description:
#       <This program provides the user with essential information in terms of their gross pay, and calculates taxes depending on their inputed values.>
#        
#
#===========================================================

# Show application header
print ("\n" * 40)  # This is needed to clear the screen
print ("Welcome to Matthew's Pays and Taxes Calculator!")
print ("--------------------------\n")

# <This code prompts the user by requesting them for their hourly rate, and their time worked in hours.>
hourly_Rate = float(input("What is your hourly rate? : "))
time_worked = int(input("How many hours did you work today? : "))

# This will calculate the user's hourly rate and time worked, in order to produce their gross pay.
gross_pay = hourly_Rate * time_worked

print ("Gross pay:   ${0:10.2f}".format(gross_pay))

# This clears the screen to display a clear view of tax calculations below, and informs the user that the following calculations below are their taxes.
print ("\n" * 1)
print ("Based on the information you've provided, these are the taxes:")
print ("===============================================================\n")
# This code provides the user with calculations of their taxes dependent on their inputted values.

# The variable "federal_tax" provides the user with their federal tax based on the calculation below.
federal_Tax = gross_pay * 0.15

print ("federal_Tax:   ${0:10.2f}".format(federal_Tax))

#The variable "fica_tax" provides the user with their fica tax based on the calculation below.
fica_tax = gross_pay * 0.0765

print ("fica_tax:   ${0:10.2f}".format(fica_tax))

#The varibale "state_tax" provides the user with their state taxes based on the calculation below. 
state_tax = gross_pay * 0.0435

print ("state_tax:  ${0:10.2f}".format(state_tax)) 

#The variable "net_pay" provides the user with their net pay based on the calculation below.
net_pay = gross_pay - federal_Tax - fica_tax - state_tax

print ("net_pay:  ${0:10.2f}".format(net_pay))
print ("======================================")
#This prompt informs the user that the calculations have been completed.
print ("Thank you for using Matthew's Pays and Taxes Calculator!")
