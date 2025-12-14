# x  = (1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9)
# print(x) 
# print(x[-1])
# # for i in x:
# #     print(i)
# print(x.count(5))
# print(x.index(2))

l1 = ["whisk", "dart", "dash"]
l2 = ["whit", "scarp", "bit"]
store = l1+l2
l2.extend(store)
print(store)
print(l2) 

l1 = ("whisk", "dart", "dash")
l2 = ("whit", "scarp", "bit")
store = l1+l2
print(store)
# l2.extend(store)  tuple has no attribute extend so error occure 

store = l2*3
print(store)

x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
(Rohan, *aditya, Rakesh) = x
print(Rohan)
print(Rakesh)
print(aditya)

(Rohan, Rakesh, *aditya) = x
print(Rohan)
print(Rakesh)
print(aditya)
