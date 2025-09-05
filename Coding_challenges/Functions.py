# FUNCTION - simple add, sub, mul, div  ##

# Function : block of reusable code that performs specific task.

# Example: 

def add():
    print("addition")
    a=int(input("enter a value: "))
    b=int(input("enter a value: "))
    print(a+b)
add()

Input => a = 10, b = 20
Output => 30

def sub():
    print("subtraction")
    a=int(input("enter a value: "))
    b=int(input("enter a value: "))
    print(a-b)
sub()

Input => a = 20, b = 10
Output => 10

def mul():
    print("multiplication")
    a=int(input("enter a value: "))
    b=int(input("enter a value: "))
    print(a*b)
mul()

Input => a = 10, b = 20
Output => 200

def div():
    print("division")
    a=int(input("enter a value: "))
    b=int(input("enter a value: "))
    print(a/b)
div()

Input => a = 20, b = 10
Output => 2

## find even or odd ##

def findevenorodd(b):
    if (b%2==0):
        print("Even")
    else:
        print("Odd")
        
a=int(input("enter a num: "))
findevenorodd(a)

Input => 15
Output => Odd

## find pass or fail ##

def passorfail(a):
    if (a>=35):
        print("Pass")
    else:
        print("Fail")
a=int(input("Enter a Mark: "))
passorfail(a)

Input => 50
Output => Pass

## find range between two numbers ##

def findrange(R1,R2):
    for i in range(R1,R2):
        print(i)

a=int(input("Enter a: "))
b=int(input("Enter b: "))
findrange(a,b)

Input => a = 5, b = 10
Output => 5
          6
          7
          8
          9

## find username true or false ##

D_username="Maadhu"
D_password="Madhu1661"

L_username=input("Enter a username: ")
L_pass=input("Enter a password: ")

def validate():
    if (D_username==L_username and D_password==L_pass):
        return "correct"
    else:
        return "Wrong"
        
a=validate()
print(a)

Input => L_username = Maadhu, L_pass = Madhu1617
Output => Wrong


## find (a+b)*c ##

def add(n1,n2):
    return n1+n2

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

addition=add(a,b)
output=addition*c
print(output)

Input => a = 10, b = 20, c = 5
Output => 150
