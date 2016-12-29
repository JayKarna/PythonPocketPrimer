#Random Comment

#ONLY WORKS IN PYTHON 3.X.X

#NOTE: Does not accept decimal values.


while(1):
	c = input('Input a temperature in Celsius: ')
	try:
		int(c)
		break
	except:
		print('I\'m sorry, but ' + c + ' is not a valid temperature')

cInF = (int(c) * (9/5)) + 32
print('This temperature, in Fahrenheit, is ' + str(cInF))


while(1):
	f = input('Input a temperature in Fahrenheit: ')
	try:
		int(f)
		break
	except:
		print('I\'m sorry, but ' + f + ' is not a valid temperature')
	
fInC = (int(f) - 32) * (5/9)
print('This temperature, in Celsius, is ' + str(fInC))
