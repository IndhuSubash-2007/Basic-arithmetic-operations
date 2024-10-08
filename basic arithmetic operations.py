'''
AUTHOR: INDHU SUBASH
PROGRAM:ARITHMETIC OPERATIONS
DATE:08-10-2024
VERSION 1.1
'''
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
addition=(num1+num2)
print("The sum of num1 and num2 is:",(addition))
subtraction=(num1-num2)
print("The difference when num2 is subtracted from num1 is:",(subtraction))
multiplication=(num1*num2)
print("The product of num1 and num2 is:",(multiplication))
division=(num1/num2)
print("The quotient when num1 is divided by num2 is:",(division))
modulus=(num1%num2)
print("The remainder when num1 is divided by num2 is:",(modulus))
combination=(addition+multiplication+division)
print("The result of ((num1+num2)*num3/2)is:",(combination))