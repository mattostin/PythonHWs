#Bringing the math library 
import math

#Creating the inputs and asking for the params
print("Cylinder Surface Area Calculator")
var_radius= float(input("Enter an radius: "))
var_height= float(input("Enter an height: "))

#The variable responsible for calculating the surface area
math_calculator = 2 * math.pi * var_radius * var_height + 2 \
    * math.pi * var_radius ** 2

#Printing the user's inputs
print("The Surface area is = ",math_calculator)

#problem 1 - Area of a Trapezoid

#Asking for trapezoid values
print("Trapezoid Area Calculator")
var_a= float(input("Enter a number for a: "))
var_b= float(input("Enter a number for b: "))
var_height_2= float(input("Enter an height: "))

#The variable responsible for calculating the trapezoid area
math_calc_trap = ((var_a + var_b) / 2)*var_height_2
print("The area of the Trapezoid is ", math_calc_trap)

#problem 2 - The Volume of a Pyramid
print("Volume of a Pyramid Calculator")

#Asking for Pyramid values
var_length = float(input("Enter a number for the Length: "))
var_width = float(input("Enter a number for the width: "))
var_height_2 = float(input("Enter a number for the height: "))

#The variable responsible for calculating the area of a pyramid
vol_pyr = (var_length * var_width * var_height_2) / 3
print ("The volume of the Pyramid is", vol_pyr)

#problem 3 - Area of a Circle

#Asking for circle values
print("Area of a circle Calculator")
radius = float(input("Enter a number for the radius: "))

#The variable responsible for calculating the area of a circle
radius_ans = math.pi * radius**2

print("The area of the radius is", radius_ans)



