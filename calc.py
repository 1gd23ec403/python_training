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



