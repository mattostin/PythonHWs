import math

var_radius= float(input("Enter an radius: "))
var_height= float(input("Enter an height: "))


math_calculator = 2 * math.pi * var_radius * var_height + 2 \
    * math.pi * var_radius ** 2

print(math_calculator)