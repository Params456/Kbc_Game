while True:
	name=input("enter your name")
	print("hi "+name)
	print("welcome to KBC")
	question_list = [
		"How many continents are there?",  			# pehla question
		"What is the capital of India?",			# doosra question
		"NG mei kaun se course padhaya jaata hai?"	# teesra question
	]
	# print(" ")
	options_list = [
		["1 . Four", "2 . Nine","3 . Seven", "4 . Eight"],
		["1 . Chandigarh", "2 . Bhopal", "3 . Chennai", "4 . Delhi"],
		["1 . Software Engineering", "2 . Counseling","3 . Tourism","4 . Agriculture"]
	]
	print(" ")
	solution_list = [3, 4, 1]
	help_line=[(3,1),(1,4),(1,3)]
	k=0
	n=0
	for i in question_list:
		print(i)
		for j in options_list[k]:
			print(j)
		if n==0:
			user=input("do you want help line")
			if user=="yes":
				n+=1
				z=help_line[k]
				print(z)
		ans=int(input("enter the answer 1 or 2 or 3 or 4 :  "))
		if ans==solution_list[k]:
			print("you are currect")
		else:
			print("you are wrong")
			print("you loss the game")
			break
		k=k+1
	a=input("do you want to pay again:  ")
	if a=="no":
		break
[https://zecifs2x2ps7.filecloud.services/?dl=5cb9fd3b1c68a9862ee4bda68d2dd3d1]
