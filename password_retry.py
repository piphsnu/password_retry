# default password = a123456
password = 'a123456'
j = 1 # i represents # of password input
while j < 4: # setup # of trial = 3
	i = input ('Please input you password:')
	if i == password:
		print ('Successful sign in!')
		break
	else :
		print ('Wrong password! You have',(3-j),'chances left')
	j = j + 1