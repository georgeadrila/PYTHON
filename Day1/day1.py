# NUMBERS
# x = 1
# y = 3.393
# z = 1j

# print(type(x))
# print(type(y))
# print(type(z))

# # converting data type
# a = float(x)
# print(type(a))

# import random
# print(random.randrange(1,5)*10-4)

# python casting is the actual declaration of a variable with int, float and string

# stirngs

# a = """fjnjnkjnfjnjnf
# jnfljldlkvlk
# rmfkmkrmkrmfkrmfkmkmkvk
# rllfmrlffkk  vrmm ediemei"""
# print(a)

# strings czn be arrays in python


# a = "Hello George what a wonderful day"
# x = "hiio" in a
# print(x)

# def func1():
#     age = 20
#     date = 2001
#     txt = "My name is maswankiu and i am {} years old and i was born in {}"
#     print(txt.format(age, date))

# func1()

# +++++++++++LISTS++++++++++
# thislist = ["appe", "mango","pine"]
# thislist2 = ["appe", "mango","pine"]
# thislist[1] = "george"
# thislist.append("baboon")
# thislist.insert(1, "cartoon")
# list3 = thislist + thislist2 

# # if "appe" in thislist:
# print(list3)

# tuple = ("jjd", "hhd", "hehe")
# for x in tuple:
#     print(tuple)

# set = {"one", "two", "three"}
# for x in set:
#     print(x)

# dict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1994
# }
# # x = dict["brand"]
# for m, n in dict.items():
#     print(m, n)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# for m , n in myfamily.items():
#     print(m, n)

# print(myfamily.get("child2"))\

# a = '2'
# b = '4'
# print(a+b)

x = 0
while x < 20:
  x = x + 3
print(x)
