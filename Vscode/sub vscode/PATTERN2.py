# left half pyramid pattern using function 
x = int(input("Enter the row number : "))
def pattern(arg1):
    """This function body code is use for left half pattern"""
    y = 2*arg1-2
    for i in range(1, x+1):
        
        for j in range(1, y+1):
            print("-", end="")
        y -= 2

        for k in range(1, i+1):
            print("*", end=" ") 
        print()

# --------*
# ------* *
# ----* * *
# --* * * *
# * * * * *
value = x
pattern(value)