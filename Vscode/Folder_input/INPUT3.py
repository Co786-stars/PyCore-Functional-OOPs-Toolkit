x  = {1, 2, 3, 4, 5, 6, 7, 8, 9}
y  = {9, 8, 7, 6, 5, 4, 3, 2, 1}
z  = {1, 20, 30, 40, 50, 60, 70}

a  = x | y |z 
b  = x & y & z  
print(a)
print(b) 

p = x.update(z)
print(p)

