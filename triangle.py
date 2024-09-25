#calculating the area of a triangle using HERON formula
#Lwazi Somtsewu 
# 31 July 2024
import math
a =float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))





# lets check the validity of a triangle
if (a+b>c) and (a+c>b) and (c+b>a):
    s = (a+b+c)/2 
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    area =round(area,2)
    print(f"The area of the triangle with sides of length {a} and {b} and {c} is {area}.")

else: 
    print("Error: The input does not describe a triangle.")
    