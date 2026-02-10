import math
a = input("enter the value of a:")
b = input("enter the value of b:")

add = int(a) + int(b)
sub = int(a) - int(b)
mul = int(a) * int(b)
div = float(a) / float(b)
mod = float(a) % float(b)
pow = math.pow(int(a), int(b))
print(f"addition : {add}")
print(f"subtraction : {sub}")
print(f"multiplication : {mul}")
print(f"division : {div}")
print(f"modulus : {mod}")
print(f"power : {pow}")

