# Q1. Python Program To Check Leap Year

year = int(input("Enter the Year "))

if (year % 400 == 0) and (year % 100 == 0):
    print(f"   {year} is a leap Year") 
elif (year % 4 ==0) and (year % 100 != 0):
    print(f"   {year} is a leap Year") 
else:
    print(f"   {year} is not a  leap Year")

# output :
# Enter the Year 2018
#    2018 is not a  leap Year
# 
#     Enter the Year 2024
#    2024 is a leap Year