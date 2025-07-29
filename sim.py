# age = int(input("Enter your age: "))

# if age < 10:
#     print("You are a child")
# else:
#     print("You are not a child")
#     num= int(input("enter a number: "))
# for i in range (1,num+1):
#     print(i)
# print("loop completed")
# if num % 2 ==0:
#     print("the number is even")
# else:
#     print("the number is odd" )
# cars = ["ford","volvo","bmw","tata"]
# print(len(cars))
# print(cars[3])

# for i in range(len(cars)):
#     print(cars[i])

   
# age = int(input("Enter your age: "))

# if age < 10:
#     print("You are a child")
# else:
#     print("you are not a child")
# num = input("enter num 1")
# num2 = input("enter num 2")

# if num.isnumeric() == False:
#     print("num1 is not number")
# elif num2.isnumeric() == False:
#     print("num2 is not number")
# else:
#     res = int(num)+int(num2)
#     print(str(res))
#num = input("enter num 1")
# num2 = input("enter num 2")

# if num.isnumeric() == False:
#     raise("num1 is not number")
# elif num2.isnumeric() == False:
#     raise("num2 is not number")
# else:
#     res = int(num)+int(num2)
#     print(str(res))
# except Exception as e:
#     print(e)
# try:
#     number = int(input("entre a number: "))
#     if number > 100:
#     raise ValueError("number is greter than 100!")
#     print(f"number {number} is whithin the all range.")
#     expect valueError as e:
#     print(f"error:{e}")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number:"))
# try:
#     if not (a.isnumeric() and b.isnumeric() and c.isnumeric ()):
#         raise ValueError("inpur must be number")
#     else:
#         if a >= b and a >= c:
#             print("the biggest number is:",a)
#         elif b >= a and b >= c:
#             print("the biggest number is:",b)
#         else:
#             print("the biggest number is:",c)
# except Exception as e:
#     print("An error occurred:",e)

num= input("Enter a number: ")
num1 = input("Enter a number: ")
opp = input("enter an operator (+,-,*,/):")

if num1.isnumeric() and num2.isnumeric():
    raise ValueError("input must be number")
else:
    case opp:
    when "+":
        result = num1 + num2
    case opp:
     when "-":
        result = num1 - num2
    case opp:
     when "*":
        result = num1 * num2
     when "/":
     if num2 !=0:
        result = num1 / num2
    else:
        raise ValueError("Cannot divide by zero")
    break
    print("the result "):")



