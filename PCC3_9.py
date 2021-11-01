invites = ['hardik', 'akshay', 'satyan']
print(f" {invites[0]} you are invited to my dinner party")
print(f" {invites[1]} you are invited to my dinner party")
print(f" {invites[2]} you are invited to my dinner party")
print(f" {invites[2]} can't make it")
invites[2] = "jim"
print(f" {invites[0]} you are invited to my dinner party")
print(f" {invites[1]} you are invited to my dinner party")
print(f" {invites[2]} you are invited to my dinner party")
print("Hey, I found out a bigger dining table")
invites.insert(0,'john')
invites.insert(3,'sally')
invites.append('raman')
print(f" {invites[0]} you are invited to my dinner party")
print(f" {invites[1]} you are invited to my dinner party")
print(f" {invites[2]} you are invited to my dinner party")
print(f" {invites[3]} you are invited to my dinner party")
print(f" {invites[4]} you are invited to my dinner party")
print(f" {invites[5]} you are invited to my dinner party")
print("Sorry, I can only invite two people for dinner")
sorry1 = invites.pop();
print(f" sorry {sorry1} for not inviting you.")
sorry2 = invites.pop();
print(f" sorry {sorry2} for not inviting you.")
sorry3 = invites.pop();
print(f" sorry {sorry3} for not inviting you.")
sorry4 = invites.pop();
print(f" sorry {sorry4} for not inviting you.")
print(f" {invites[0]} you are still invited to my dinner party")
print(f" {invites[1]} you are still invited to my dinner party")
print(f"I have invited {len(invites)} people for dinner")