#All Arithemetic Operations with python

def add(a,b):
    print(a+b)
    ch=raw_input("Want to try again ?");
    if ch=='y':
        options()

def sub(a,b):
    print(a-b)
    ch=raw_input("Want to try again ?");
    if ch=='y':
        options()

def mul(a,b):
    print(a*b)
    ch=raw_input("Want to try again ?");
    if ch=='y':
        options()

def div(a,b):
    print(float(a)/float(b))
    ch=raw_input("Want to try again ?");
    if ch=='y':
        options()

def options():
    
    print("Welcome to the Arithemetic Operations World")
    choice=input("Enter the Choice \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division\n 5.Quit\n")
    if choice < 5:
        print("Enter Two numbers for Arithemitic Operations:")
        a=input("Enter the First Number: ")
        b=input("Enter the Second Number: ")
        if choice == 1:
            add(a,b)
        elif choice == 2 :
            sub(a,b)
        elif choice == 3:
            mul(a,b)
        elif choice == 4:
         div(a,b)

    elif choice==5:
        import sys;
        sys.exit();
         
    elif choice>5 :
        print("Wrong Option");
        ch=raw_input("Want to try again ?");
        if ch=='y':
            options()
a=0
b=0
options()
