# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {2} pieces of item number {1} for {0:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# from pyexpat import model


# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = "Lamborghini" , model = "Veneno"))

# f = open("demofile.txt", "r")
# print(f.read())
# print(f.readline())
# print(f.readline())
# for x in f:
#     print(x)
# f.close()

# f = open("demofile.txt", "a")
# f.write("Now my file has more content")
# f.close()

# f = open("demofile.txt", "r")
# print(f.read())


# f = open("file.txt", "x")

import os
os.remove("file.txt")
