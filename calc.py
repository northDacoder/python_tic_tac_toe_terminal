#building a calculator
"""
Make a calculator that has basic and advanced functionality.  Let the user pick which one they want.
Basic calculator will have addition, subtraction, multiplication, and division
Advanced calculator will have exponents and square roots
"""

import math


# Basic Calculator 
def basic_calc(response):
	while (response != "q"):

		if response == "add":
			num_one = int(raw_input("Enter the first number to add"))
			num_two = int(raw_input("Enter the second number to add"))
			print "Addition: " 
			print num_one + num_two

		elif response == "substract":
			num_one = int(raw_input("Enter the first number to subtract"))
			num_two = int(raw_input("Enter the second number to subtract"))
			print "Subtraction: " 
			print num_one - num_two

		elif response == "multiply":
			num_one = int(raw_input("Enter the first number to multiply"))
			num_two = int(raw_input("Enter the second number to multiply"))
			print "Multiplication: " 
			print num_one * num_two

		elif response == "divide":
			num_one = int(raw_input("Enter the first number to divide"))
			num_two = int(raw_input("Enter the second number to divide"))
			print "Division: " 
			print num_one / num_two


# Advanced Calculator 
def advanced_calc(response):
	while  (response != "q"):

		if response == "exponents":
			number = int(raw_input("Enter the number"))
			exponent = int(raw_input("Please enter the exponent"))
			print "Exponents: " 
			print math.pow(number, exponent)

		elif response == "squareroots":
			num_one = int(raw_input("Enter the number you would like to find the square root for"))
			print "Square Root: "
			print math.sqrt(num_one)


# Choose type of calculator to use ("basic" or "advanced")
def choose_calc(type):

	if type == "basic":
		response = raw_input("What operation would you like to perform? (Please add, subtract, multiply, or divide) ")
		currentCalc = "basic"
		print "Loading basic calculator"
		basic_calc(response)

	elif type == "advanced":
		response = raw_input("What operation would you like to perform? (Please select exponents or squareroots) ")
		currentCalc = "advanced"
		print "Loading advanced calculator" 
		advanced_calc(response)



calcType = raw_input("Please select the type of calculator you would like to use (Please select basic or advanced) ")
choose_calc(calcType)
currentCalc = ""


if (response == "q"):
	print "Thanks for using the calculator!"





