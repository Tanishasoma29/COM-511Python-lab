
def add(x,y):
return x+y
def subtract(x,y):
return x-y 
def multiply(x,y):
return x*y 
def divide(x,y):
if y!=0:
return x/y 
else:
return "Cannot divide by zero"
while True:
print("Options:")
print("1: Add\n2: Subtract\n3: Multiply\n4: Divide\n5: Exit")
choice = int(input("Enter Choice(1-5): "))
if choice in [1,2,3,4]:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice==1:
print("Result: ",add(num1,num2))
elif choice==2:
print("Result: ",subtract(num1,num2))
elif choice==3:
print("Result: ",multiply(num1,num2))
elif choice==4:
print("Result: ",divide(num1,num2))
elif choice==5:
print("Exiting the calculator.Goodbye!")
break
else:
print("Invalid input. Please enter a number between 1 and 5.")
