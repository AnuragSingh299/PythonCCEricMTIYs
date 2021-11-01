current_users = ['ANURAG', 'ANMOL', 'JAKE', 'KARIM', 'RAJAN']
current_users = ['anuarg', 'anmol', 'jake', 'karim', 'rajan']
new_users = ['jim', 'anmol', 'smith' ,'hari' ,'karim', 'ganesh']
for new_user in new_users:
	if new_user in current_users:
		print(f"{new_user} needs to add a new user name.")
	else:
		print(f"{new_user} user name is available.")