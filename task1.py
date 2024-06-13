#Input two numbers and print their sum

#a = int(input("enter first number:"))
#b = int(input("enter second number:"))
#sum = a + b
#print("total sum is:",sum)


#Input side of the square and print its area

#a = float(input("enter the side length of the square:"))
#area = a*a
#print("area of the square is:",area)

#Input two floating point numbers and print their average

#a = float(input("enter the first floating point number:"))
#b = float(input("enter the second floating point number:"))
#average = (a + b)/2
#print("average of two floating point is",average)


#Input two int numbers a & b, print true if a is greater then or equal to if not print false

#a = int(input("enter the first integer (a)"))
#b = int(input("enter the second integer(b)"))
#if a >= b:
 #   print(True)
#else:
 #   print(False)


#input users first name and print its length
#name = str(input("Enter your first name:"))
#print(len(name)) 


#find the occurrence of '$' in string
#str = 'The symbol of the doller is $'
#print(str.count("$"))


#check if a number entered by a user is even or odd
number = int(input("Enter a number:"))
if number % 2 == 0 :
    print("the number is an even number.")
else:
    print("the number is a odd number6")


#find the greatest of three numbers entered by the users
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
print("the greatest number is:",greatest) 


#To check if a number is multiple of 7 or not
number = int(input("Enter a number:"))
if number % 7 == 0:
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")



