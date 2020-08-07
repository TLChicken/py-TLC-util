

def menu(qn, *args):
	counter = 0
	ansList = []
	for ans in args:
		counter = counter + 1
		ansList.append(str(counter) + ". " + ans)

	print(qn)
	for ans2 in ansList:
		print(ans2)
	notChosen = True

	while notChosen:
		choice = input("Enter the corresponding number for the answer you choose.\n")
		try:
			choice = int(choice)
			if choice > 0 and choice < len(ansList) + 1:
				return choice
			else:
				print("Please enter one of the choices listed.")
		except:
			print("Please enter a valid integer.")



		
thing = menu("hi", "ans1", "ans2", "ajndskd", "292993", "wow")
print (str(thing) + "was chosen.")	



