"""
-> An import statement tell python to make the code in a module available in the currently running program file 

-> A module is a separate file that contains functions, classes, and variables, which we create for reuse in other
   programs or modules or importing that module in main program 

-> Storing the function in a saperate file allow to hide the details of programs code and focus on high-level logic  

-> There are many ways to import modules modules : -
   1)) import the entire module
   2)) import the specific function 
   3)) using as to given a function an alias 
   4)) using as to give a module an alias 
   5)) importing all the function in module 

-> The code that not written under the function excute by default in saperate file (modle3) output but the code that 
   written under the function only excute when we import that function using import keyword .  

->  The 'as' keyword in the import statement used to create an alias for the imported module or function.

->  The name alias ['as'] means alternate name for the function that can make your code more readable or help avoid 
    naming conflicts.

""" 

# WAP to swipe two number using basic logic of boadmass

def  swipe_function(value1, value2):
    """swipe function"""
    value =  value1+value2
    value1 = value - value1
    value2 = value - value2  
    return value1, value2  
 
# Wap to multiply two number without using multiply signs

# 6 x 3 =  6 6 6  
def multi(num1, num2):
    """Multiply of two number without using astrisk symboll"""
    multi = 0
    for i in range(1, num2+1):
        multi += num1    # That is the concept of multiplication 4 X 3 =  4 4 4  
    return multi

# Wap to print the factorial of the number for example 6 = 6! x 5! x 4! x 3! x 2! x 1! >> 720

def factorial(f_value):
    """ Factorial of a number with using multiply symboll """
    if f_value == 0:
        return 1
    
    num = f_value
    fact = 1
    for i in range(1, f_value+1):
        
        print(f"{num}! ", end=" ")
        fact *= num
        num -= 1
    print(f": {fact}")


# wap to print factorial number without using multipal operator 6 = 6!  5!  4!  3!  2!  1! >> 720
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         temp = 0
#         for j in range(result):
#             temp += i
#         result = temp
#         print(result)
#     return result

# number = 5
# print(f"The factorial of {number} is {factorial(number)}")
