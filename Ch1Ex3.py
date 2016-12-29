#Receive input from user, and make sure it is not an int or float
while(1):
	text = input('Input a line of text: ')
	try:
		int(text)
		print('I\'m sorry, please try again')
	except:
		try:
			float(text)
			print('I\'m sorry, please try again')
		except:
			break		

#Capture first and last character
start = text[:1]
end = text[-1:]

print('The first character is ', start, ' and the last character is ', end, '.')