#Q2. Using input function take two numbers
# and then swap the numbers

a , b = input("Enter the two  numbers seperated by space").split()
print(f"before swaping a:  {a}, b :{b}")

a , b = b , a 
print(f"after  swaping a:  {a}, b :{b}") 

#####output###

# Enter the two  numbers seperated by space3 4
# before swaping a:  3, b :4
# after  swaping a:  4, b :3