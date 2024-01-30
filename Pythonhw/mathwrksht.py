#Bringing the math library 
import math

#Creating the inputs and asking for the params
var_radius= float(input("Enter an radius: "))
var_height= float(input("Enter an height: "))

#The variable responsible for calculating the surface area
math_calculator = 2 * math.pi * var_radius * var_height + 2 \
    * math.pi * var_radius ** 2

#Printing the user's inputs
print(math_calculator)