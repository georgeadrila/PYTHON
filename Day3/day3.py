# class person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname

#     def printname(self):
#         print(self.fname, self.lname)

# m = person("George", "Adrian")
# m.printname()


# class student(person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.gradyear = year


# n = student("Aaaaa", "Bbbbb", 2019)
# print(n.gradyear)


# +++++++++++ PYTHON ITERATORS +++++++++++++++ #

# mytuple = ("apple", "banana", "sweet")
# myit = iter(mytuple)

# # print(next(myit))
# # print(next(myit))
# # print(next(myit))

# for x in mytuple:
#     print(x)

# class numbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration


# myclass = numbers()
# myiter = iter(myclass)

# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))

# for x in myiter:
#     print(x)


# for x in range (1, 16, 4):
#     print(x)

# def myfunc():
#     global x
#     x = 20
#     print(x)
# myfunc()

# print(x)

# import modules

# modules.greeting(" George")

import platform

x = platform.system()
print(x)


 