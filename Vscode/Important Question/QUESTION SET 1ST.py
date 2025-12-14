'''# 12 )) Solution

# 11 )) Solution
""" name = Aditya Raj
 Current_date = 28-02-2024
"""


# 10 )) Solution

fav_number = 45
massage = f"My favorite number is : {fav_number}"
print(massage)

# >> Note : --


num1 = "wizard hacker "
print(f"Hello {num1}")
print(f"hello {num1}".upper())
print(f"hello {num1}".casefold())
print(f"Hello {num1}".swapcase())
print(f"hello {num1.upper()}")
x = "Ny NAME IS Aditya Raj saurab singh rajput"
print(x.upper())
print(f"This is upper : {x.upper()}")
print(f" this is num1 {num1} ".upper())



# 09 )) Solution

print(7+1)          # addition operation
print(9-1)          # subtraction operation
print(4*2)          # Multiplication operation
print(16//2)        # Division operation in int value
print(16/2)         # Division operation in float value

# 08 Solution

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

# >> Note : --
remove_pre = "https:/hello_world"
print(remove_pre.removeprefix("https:/"))


# 07 Solution

person_name = "\tHidden wizard\t"
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())


# 06 Solution

famous_person = "Mathma Gandhi"
massage = f"{famous_person} say's simple living higher thinking si better way to living your life"
print(massage)

# 04 Solution

your_name = "Person_name"
print(your_name.lower())
print(your_name.upper())
print(your_name.title())
print(your_name.swapcase())
print(your_name.casefold())

# 03 Solution

name = "Hello Aditya"
msg = f"{name} How are you ? "
print(msg)


# 02 Solution

name = "vipasa"
l_name = "kumari"
print(l_name)

# 01 Solution

x = "your msg"
print(x)

'''

"""# LIST PRACTIC
x = ["Red", "Yellow", "Pink", "Green"]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x.append("Purple")
x.insert(0,"White")
x.extend(y)
print(x)
# NULL LIST
z = []
z.append(10)
z.append(11)
z.append(12)
z.append(13)
_ADD_ = [15, 16, 17, 18, 19, 20]
z.extend(_ADD_)
print(z)

alpha = ["a", "b", "c", "d", "e"]
alpha.pop()
print(alpha) # Automatically delete the last item in list
alpha.pop(0) # Use to delete index value at any position
print(alpha)"""
# del alpha
# print(alpha)

"""
z  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(z)
z.remove(5)
print(z)
del z[5]
print(z)
del z
# print(z)


x = [10,11,12,13,14,15,17,18,19,20]
for i in x:
    print(i)

x = [1,2,3,4,5,6,7,8,9,10]
for i in x:
    print("xgjkng")


for i in range(len(x)
               ):
    print(i, end=" ")
"""

"""
z = ["Hello", "Everyone", "How", "are", "You"]
i = 0
while i < len(z):
    print(z[i], end=" ")
    i += 1

print("\n")

[print(i) for i in z]

new_list = ["value1", "value2", "value3", "value4", "value5", "value6"]
other_new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in new_list:
    print(i)
    if i == "value3":
        for j in other_new_list:
            print(j)


my_names = ["wizard", "harry", "honey", "petter"]
sel_name = []
for name in my_names:
    if "e" in name:
        sel_name.append(name)
        sel_name.extend(my_names)
        print(name)

print(sel_name)
print(my_names)
"""
# shorthand loop with list syntax >>> [expression for item in iterable if condition == True]
#
# x = ["aditya", "Rohan", "Sohan", "Prakash", "abhishek"]
# [print(i, end=" ") for i in x]
#
# print("\n")
# for i in x:
#     print(i , end=" ")
print("\n")




# from turtle import *
# bgcolor("black")
# color("Cyan")
# speed(15)
# right(45)
# for i in range(150):
#     circle(20)
#     if 7< i < 62:
#         left(5)
#     if 80 <i <133:
#             right(5)
#     if i< 80:
#         forward(10)
#     else:
#         forward(5)
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list= [new for new in x]
print(list)

l_1 = [x for x in range(10) ]
print(l_1)

l_2 = [x for x in range(11) if x > 5]
print(l_2)

table = [10*x for x in range(1, 50) if x<=10]
print(table, end="\n")

l_3 = ["red", "green", "blue", "pink", "yellow"]
case_1 = [store.upper() for store in l_3]
print(case_1)

l_4 = ["red", "green", "blue", "pink", "yellow"]
case_2 = [continar.title() for continar in l_4 if continar != "yellow"]
print(case_2)

l_4 = ["red", "green", "blue", "pink", "yellow"]
case_2 = [continar.upper() for continar in l_4 if continar != l_4.pop()]
print(case_2)


x =[10, 20, 30 , 40, 50, 60 , 70, 80, 90]
insert_value = [100 for y in x ]
print(insert_value)

print("\n")
x = [9, 3, 2, 4, 5, 6, 10, 8, 1, 7]
x.sort()
print(x)
x.reverse()
print(x)

y = ["b", "c", "i", "e", "a", "k", "h", "g", "j", "d"]


print(sorted(y))
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.sort(reverse = True)
print(y)

l = [1 , 9 , 8 , 7]
l.sort(reverse = True)
print(l)


case  = ["zebra", "Monkey", "Rabbit", "elephant"]
case.reverse()
print(case)

cone = case.copy()
print(cone)

list1  = [2,3,4,5]
list2 = [1,6,7,8,9,10]
print(list1+list2)
x = list1+list2
print(x)
x.sort()
print(list1+list2)
print(x)


other_list = ["apple", "orange", "banana"]
other_2nd_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in other_2nd_list:
    other_list.append(i)
print(other_list)

x, y = 67 , 100
txt ="{1} {0}"
print(txt.format(x , y))
