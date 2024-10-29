#sai
# def addition(a,b):
#     c=a+b
#     print(c)
# def subtraction(a,b):
#     c=a-b
#     print(c)
# def multiplication(a,b):
#     c=a*b
#     print(c)
# def division(a,b):
#     c=a/b
#     print(c)
# def power(a,b):
#     c=a**b
#     print(c)
# def remainder(a,b):
#     c=a%b
#     print(c)
#
# a = int(input("Enter first number "))
# b = int(input("Enter second number "))
# operation = input("choose your operation + * ** / %  :  ")
# if operation == "+":
#     addition(a,b)
# if operation == "-":
#     subtraction(a,b)
# if operation == "*":
#     multiplication(a,b)
# if operation == "**":
#     power(a,b)
# if operation == "%":
#     remainder(a,b)
# if operation == "/":
#     division(a,b)


#Pradeep
def calculator (num1,num2,operator):
    if operator=="*":
        print(num1*num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="+":
        print(num1+num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "%":
        print(num1 % num2)
    elif operator == "**":
        print(num1 ** num2)

stop_indicator = False
while not stop_indicator:
  num1=int(input("Enter the 1st Number :"))
  num2=int(input("Enter the 2nd Number :"))
  operator=input("Enter the operator")
  calculator(num1,num2,operator)
  stop_indicator_value=input("Enter stop if you want to stop the program :")
  if stop_indicator_value.lower() =="stop":
      stop_indicator = True



