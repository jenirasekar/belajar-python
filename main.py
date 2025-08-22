# append items
# fruits = ["apple", " orange", "banana"]
# fruits.append("orange")
# print(fruits)

# insert items
# fruits = ["apple", "banana", "cherry"]
# fruits.insert(0,"orange")
# print(fruits)

# list comprehension
# fruits = ["apple", "banana", "cherry"]
# new_fruits = []
# for x in fruits:
#     if "a" in x:
#         new_fruits.append(x)
#         print(new_fruits)
#
# # newlist = [expression for item in iterable if condition == True]
# new_fruits = [x for x in fruits if "a" in x]
# new_fruits.append("durian")
# print(new_fruits)

# sort list alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)