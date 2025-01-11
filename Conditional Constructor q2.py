# Q2 Python Program to find largest among 
# three numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 == num2 == num3:
    print(f"All three numbers are equal: {num1}")
elif num1 == num2 and num1 > num3:
    print(f"The largest numbers are equal: {num1} and {num2}")
elif num1 == num3 and num1 > num2:
    print(f"The largest numbers are equal: {num1} and {num3}")
elif num2 == num3 and num2 > num1:
    print(f"The largest numbers are equal: {num2} and {num3}")
elif num1 >= num2 and num1 >= num3:
    print(f"The largest number among {num1}, {num2}, and {num3} is {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number among {num1}, {num2}, and {num3} is {num2}.")
else:
    print(f"The largest number among {num1}, {num2}, and {num3} is {num3}.")
 
 #########################
# #  Output
# Enter the first number: 10
# Enter the second number: 10
# Enter the third number: 10
# All three numbers are equal: 10.0

# Enter the first number: 12
# Enter the second number: 13
# Enter the third number: 12
# The largest number among 12.0, 13.0, and 12.0 is 13.0.
# PS F:\WEPP\Lab> 
 
# Enter the first number: 12
# Enter the second number: 11
# Enter the third number: 34
# The largest number among 12.0, 11.0, and 34.0 is 34.0.
# PS F:\WEPP\Lab> 