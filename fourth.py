def area_of_triangle(side_a,side_b,side_c):

 s = ((side_a+side_b+side_c)/2)
 triangle_area=(s*(s-side_a)*(s-side_b)*(s-side_c))**0.5
 print(f"The Area Of Triangle of given sides {side_a} , {side_b} and {side_c} is : {round(triangle_area,2)}")


area_of_triangle(5,5,5)
area_of_triangle(4,5,6)