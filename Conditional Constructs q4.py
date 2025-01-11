"""
A toy vendor supplies three types of toys: 
Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.
 The vendor gives a discount of 10% on orders for battery-based toys
if the order is for more than Rs. 1000.
on orders of more than Rs. 100 for key-based toys, a discount of 5% is given, 
and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. 
Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, 
and electrical charging based toys respectively. Write a program that reads the product code 
and the order amount and prints out the net amount that the customer is required to pay after the discount.
"""
product_code = int(input("Enter the product code"))
# order_amount = int(input("Enter the product amount"))
discount = 0
if  product_code == 1 or product_code == 2 or product_code == 3:
 order_amount = int(input("Enter the product amount"))

 if product_code == 1:
    if order_amount > 1000:
        discount = order_amount * 0.10
    print(f"The Net amount is : {order_amount - discount} " )
 elif product_code == 2:
    if order_amount > 100:
        discount = order_amount * 0.05
    print(f"The Net amount is : {order_amount - discount} " )               
 elif product_code == 3:
    if order_amount > 500:
        discount = order_amount * 0.10
    print(f"The Net amount is : {order_amount - discount} " )  
else:
    print("Invalid Key Please enter correct key")  

###########################OUTPUT    
"""
Enter the product code4
Invalid Key Please enter correct key 

Enter the product code1
Enter the product amount1001
The Net amount is : 900.9 
 
Enter the product code2
Enter the product amount2400
The Net amount is : 2280.0 
 
Enter the product code3
Enter the product amount100
The Net amount is : 100  
 
""" 