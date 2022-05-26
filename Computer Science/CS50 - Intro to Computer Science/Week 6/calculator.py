# V0
# try: 
#     x = int(input("x: "))
# except ValueError:
#     print("That is not an int!")
#     exit()
# 
# try:     
#     y = int(input("y: "))
# except ValueError:
#     print("That is not an int!")
#     exit()
# 
# print(x + y)

# V1

from cs50 import get_int
x = get_int("x: ")
y = get_int("y: ")

z = x / y

print(z)
