#usernames = ['anurag', 'anmol', 'harshit', 'admin', 'jason']
usernames = []
if usernames:
	for username in usernames:
		if username == 'admin':
			print(f"Hello {username} would you like to see a status report?")
		else:
			print(f"Hello {username} thankyou for logging in again")
else:
	print("We need to find some users!")