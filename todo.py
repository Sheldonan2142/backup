# Abigail Sheldon Class 4
# To-Do list
print("Welcome friend to the To-Do list :)")
todoList = []
while True:
	print("press a to add to the list !")
	print("press r to remove from the list !")
	print("press p to print the list !")
	print("press q to quit uwu")

	choice = input("What will you press~? ")
	if choice == "a":
		todo = input("what would you like to add, friend ? ")
		todoList.append(todo)
	elif choice == "r":
		index = int(input("which number on the list would you like removed, friend ? "))
		todoList.pop(index)
	elif choice == "p":
		print(todoList)
	elif choice == "q":
		break
	else:
		print("sorry i dont understand, friend :( ")

