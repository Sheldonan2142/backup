# abigail sheldon class 4

#variable declaration and assignment 
# examples
myNum = 12 #integer type
myString = "12" #string type
myNum + 3 #will work
print(myString + "3") #will not work

# make a variable and assign it the value of your favorite movie
# print "my favorite movie is" followed by the variable

myFav = "High School Musical 2"
print("My favorite movie is " + str(myFav))

# while loops
# example - print from 1 to 10

x = 1
while x <= 10:
	print(x)
	x = x + 1 

# count down from 100 using a while loop
x = 100
while x >= 0:
	print(x)
	x = x-1

# string concatenation
# means putting two strings together 

myName = "CODEL"
print("Hello "+ myName)

yourName = input("what is your name? ")
print("Hello " + yourName +" have a nice day")
number = input("Enter a number: ")
number = int(number) + 10
print("The number is " + str(number))
# ask for 2 numbers, add them and print the sum
number1 = int(input("Enter a number!: "))
number2 = int(input("Enter another number: "))
answer = str(number1+number2)
print("The sum of these numbers is: " +answer)

# if / else statements
numm = int(input("Enter a number: "))
if numm > 100:
 	print("Your number is p/ large huh? ")
elif numm == 100:
 	print(" you put 100 didnt you")
else:
 	print("what a weak number")

 # ask if today is your birthday

birth = input("is today your day of birth, friend? answer yes or no: ")
if birth == "yes":
	print("thats so coooool wow congrats")
elif birth == "no":
	print("it will be s o o n")
else:
	print("wait try again i cant read")