"""# Question 13 ))
names = ["Abhishek", "Rohit", "Aditya", "wizard", "Hacker"]
print(names)

for name in names:
    print(name)

name = 0
while name < len(names):
    print(names[name])
    name += 1

short_hand = [x for x in names]
print(short_hand)


for name in names:
    print(f"Friend name : {name}")


f_name = 0
while f_name < len(names):
    print(f"My friends {f_name} name is : {names[f_name]}")
    f_name += 1



# short_hand = [x for x in names if x == "Aditya"]
# print(short_hand)


print("\n\n")
# Question 14 ))  >> Question is related to Question number 13

for friend_name in names:
    print(f"Hello {friend_name} How are you ? ")



print("\n\n")
# Question1 15 ))

van = ["car", "motorcycle", "bycycle" , "Aeroplane", "Ship"]
print(f"I would like to own van {van[1]}")

motorcycle = ["Apache", "Hero", "Honda", "Bmw", "KTM"]
print(f"I would like to own {motorcycle[2]} motorcycle ")
for favorite in motorcycle:
    print(favorite)
    if favorite == "Honda":
        print(f"My would like to own {motorcycle[2]}")

print("\n\n")
# Question 13 , 14 ))

friends_name = ["Ronaldo", "Trump", "Charlie", "Donald"]
name = 0
while name < len(friends_name):
    print(f"Hello how are you {friends_name[name]}")
    name += 1

while name < len(friends_name):
    print(f"Hello how are you {friends_name[name]}")
    name += 1

"""

"""# Question 16 ))
guest = ["jack", "pale", "woods", "stephen", "lei"]
for invite_guest in guest:
    print(f"pls {invite_guest} let's take a dinner")



guest.insert(0,"rocky")
guest.insert(3, "lya")
guest.append("Myra")


for x in guest:
    guest.pop()
print(guest)
"""

"""# Question 18 (3.8)

place = ["india", "Australia", "England", "Japan"]
print(place)
print(sorted(place))
print(sorted(place))
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.sort(reverse=True)
print(place)
print(len(place))

"""

# Question 19 ))

mountain = ["Mount everest", "Himalaya", "Mount kilimanjaro"]
countries = ["india", "nepal", "bhutan", "srilanka"]
cities = ["patna", "kolkata", "New York", "mumbai"]
languages = ["sanskrit", "Urdu", "tamil", "hindi", "english", "telgu"]

multi_dim = [["red", "yellow", "pink", "purple", "blue", 'bright', "green", "deep"],
             ["laptop", "monitor", "keyboard", "mouse" , "radio", "tab", "speaker"],
             ["micro", "mini", "super", "quantum", "hybrid",  "analog", "digital" ]]


x = mountain[0]
print(x)
print(countries[2])
print(cities[3])
print(multi_dim[2])
print(multi_dim[1][4])
print(multi_dim[-2][-3])


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< modify list  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# negetive indexing

print("\n",mountain[-1])
print(mountain[2:3])
print(mountain[-1])
print(mountain[-3])
print(mountain[:10])


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< upper value >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print(multi_dim[0][2].upper())

upper_case_list = [u_v.upper() for u_v in cities]
print(upper_case_list)


upper_case_language = []
for x in languages :
    upper_case_language.append(x.upper())       # use to store list item in upper_case_language variable
print(upper_case_language)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< lower case >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

lower_case_language = []
i = 0
while i < len(upper_case_language):
    lower_case_language.append(upper_case_language[i].lower()) # use to store or append upper item in lower case item
    i += 1
print(lower_case_language)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< title case >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

title_case_language = [title_case.title() for title_case in lower_case_language]  # short hat loop
print(title_case_language)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< SwapCase >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


mountain = [x.swapcase() for x in mountain]
print(mountain)


for x in range(len(mountain)):
    mountain[x] = mountain[x].swapcase()
print(mountain)


# f string
message = f"My country name is {countries[0].title()}, it a beautiful country"
print(message)

# upper_case_list = [[u_v.upper() for u_v in sub_list] for sub_list in multi_dim]
# print(upper_case_list)

# List modification

print(cities)
cities =[x.upper() for x in cities]
print(cities)
cities.append("KARACHI")
cities[4] = "TOKYO"
#cities[6] = "TOKYO"   # error
cities[0] = "MUMBAI"
cities.append("KABUL")
print(cities)
cities.insert(0,"DELHI")
print(cities)
del cities
print("\n\n", countries)
del countries[3]
print(countries)
countries.pop()
print(countries)
countries.remove("nepal")
countries.remove("india")
print(countries)


print(languages)
#
# languages.remove(languages[0])
# languages.remove("hindi")
print(languages)
languages.sort()
print(languages)

x = sorted(mountain)
print(x)
x.reverse()
print(x)
print(multi_dim)
multi_dim.reverse()
print(multi_dim)
multi_dim.sort()
print(multi_dim)

# Question 20

print(x[10])   #error   happpening
