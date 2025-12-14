"""# (( Question 4.3 ))

for num in range(1, 21):
    print(num)

# (( Question 4.4 ))

x = [m_num for m_num in range(1, 1000001) ]

for million in x:
    print(million)

# (( Question 4.4 ))

print("Addition of number : ", sum(x))
print("Smallest number    : ", min(x))
print("Biggest number     : ", max(x))
"""

"""for n in range(1, 21,2):
    print(n)

print("\n", "Number 3 to 30 are given below")

list = []
for num1 in range(3, 31):
    list.append(num1*3)
print(list)

num = [x*3 for x in range(1, 21)]
print(num)
"""

# (( Question 4.8 )) :

cube = []
for n in range(1, 11):
    cube.append(n**3)
print(cube)

c_n = []
for num in range(1, 11):
    c_v = num**3
    c_n.append(c_v)
print(c_n)

# with while loop in python

i = 1
l1 = []
while i < 11:
    l1.append(i**3)
    i +=1
print(l1)

# with while loop other process
j = 1
l2 = []
while j < 11:
    cube = j**3
    l2.append(cube)
    j += 1
print(l2)

# By using list compherension

exp = [p**3 for p in range(1, 11)]
print(exp)




