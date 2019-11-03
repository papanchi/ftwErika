while True:
	try:	
		year = int(input( " Enter year: "))
	except ValueError:
		print ("\n Try again \n")
		continue
	if year >= 2000 and year <= 2100:
		print('Welcome to the 21st Century'+'\n')
	else:
		print('You are before or after the 21st century\n')