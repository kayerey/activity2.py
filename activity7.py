#confirmation of the subject

gold=0
explorer = input("input your name, explorer: ")

quality = input("is the mineral above the standards?")

if quality.lower() == "yes":
	gold += 1
	print(f"hello! {explorer}, your total minerals is {gold}")
else:
	print(f"unfortunate! {explorer}, your standards of your minerals arent fit!!")