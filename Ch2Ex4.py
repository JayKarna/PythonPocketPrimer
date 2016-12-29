def divisors(num):
	count = 1
	div = 2
	while(div < num):
		if(num%div == 0):
			count = count + 1
		div = div + 1
	return count

# "Table" heading
print('{:>5} {:>5} {:>5}'.format('i |', 'i^2 |', 'i^3'))
print('------------------')
# Cycle i through values 1 - 10.  Print i, i^2, and i^3 (converted to strings for formatting purposes)
for i in range (1, 10 + 1): 

	if (i != 1):
		
		result = divisors(i)

		if (result == 1):

			#Use string.format() to print columns.  ":>"" means using right alignment, "5" is the spacing between right alignments
			print('{:>5} {:>5} {:>5}'.format(str(i) + ' |', str(i**2) + ' |', str(i**3)))

#Require user input to close
input()