# and or or


# a = 200
# b = 33
# c = 500
# if a > b or c > a:
#     pass

# i = 1
# while i < 6:
#     print(i)
#     i += 1 

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x, y)

# def func1(name1, name2):
#     print("My name is " + name1 + name2)

# func1(name1 = "George", name2 = " Adrian")

# def func2(food):
#     for x in food:
#         print(x)

# fruits = ["maango", "apple", "weed"]

# func2(fruits)

# def func3(x):
#     return 5 * x

# print(func3(5))

# # LAMBDA FUNCTIONS
# x = lambda a,b,c : a * (b/c)
# print(x(5, 4, 2))

# ++++++++++PYTHON CLASSES++++++++++ #

# class myclass:
#     x = 5

# p1 = myclass()
# print(p1.x)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def func4(self):
#         print("Hello my name is " + self.name)
#     # def func5(self):
#     #     print("I am  " + self.age + " years old.")

# p1 = person("George. ", 20)
# p1.func4()
# p1.func5()

# print(p1.name)
# print(p1.age)

# ++++++++++PYTHON INHERITANCE++++++++++ #
class person:
    def __init__(self, name, names):
        self.name = name
        self.names = names

    def func4(self):
        print("Hello my name is " + self.name + self.names)

p1 = person("George ", "Adrian")
p1.func4()


class student(person):
    def __init__(self, name, names, age, year):
        super().__init__(name, names)
        self.age = age
        self.year = year
    
    def func5():
        print("I am " + student.age + " and i am graduating in " + student.year)

x = student("Paula ", "Adrila")
x.func4()
x.func5(20, 2002)