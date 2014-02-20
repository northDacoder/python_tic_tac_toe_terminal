import sys

def one_function(number): 
	if number % 3 == 0 and number % 5 == 0:
		print "fizzbuzz"
	elif number % 5 == 0:
		print "buzz" 
	elif number % 3 == 0: 
		print "fizz"
	else:
		print "The number is not divisible by 3 or 5, sorry!"


one_function(int(sys.argv[1]))
one_function(15)
one_function(5)
one_function(3)
one_function(19)

def two_function(x,y):
		print x
		print y
		return 23 #should only have one return in a function

print 5 * two_function(3,4) 


# number = int(raw_input('Please enter a number: '))
# for num in range(number):
# 	msg = ''
# 	if num % 3 == 0:
# 		msg += 'Fizz'
# 	if num % 5 == 0:
# 		msg += 'Buzz'
# 	print msg or num





