
#All Arithemetic Operations with python
print("Welcome to the Arithemetic Operations World")
options()    #Getting Error Here.

def add():
	print(a+b)
def sub():
	print(a-b)
def mul():
	print(a*b)
def div():
	print(a/b)

def options():
	print("Enter Two numbers for Arithemitic Operations:")
	a=input("Enter the First Number: ")
	b=input("Enter the Second Number: ")
	choice=input("Enter the Choice \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division\n 5.Quit\n")
	perform(choice)    # Error: I want to pass choice to perform function so that it will work according to the choice

def perform(choice):
	if choice!=5:
		if choice == 1:
			add()
		elif choice == 2:
			sub()
		elif choice == 3:
			mul()
		elif choice == 4:
			div()

	elif choice==5:
		import sys;
		sys.exit(0)
	else:
		print("Wrong Option");
		options()

