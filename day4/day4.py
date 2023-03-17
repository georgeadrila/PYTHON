# +++++++++PYTHON DATE TIME++++++++++ #

# import datetime

# x  = datetime.datetime.now()
# print(x)

# +++++++python json++++++

# import json

# x = '{"name":"John", "age":30, "city":"Kampala"}'

# # x parse x:
# y = json.loads(x)
# # converting from python to json we use the dump method

# # the result is  a python dictionary
# print(y["city"])

# +++++++++++++exception handling+++++++++
# try:
#     print(m)
# except:
#     print("An exception error occured")


# try:
#     print("Hello George")
# except NameError:
#     print("Variable m is not defined")
# except:
#     print("Something else is wrong")
# else:
#     print("Nothing went wrong")
# finally:
#     print("The try except is finished")




x = -3

if x < 0:
    raise Exception("Sory, no numbers below zero")