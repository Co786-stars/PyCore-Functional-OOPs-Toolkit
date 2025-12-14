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

-> The astrisk symbol in the import statment tell python to copy every function from the module in main function or saperate file 

"""


# for entire module  # >> import modulename
import modle4 
modle4.factorial(5)


# for specific function # >> from modulename import fun1, fun2 ...etc
from modle4 import swipe_function
print(f"{swipe_function(4, 5)}")



# for module as alias  # >> import modulename as mn
import modle4 as md4
print(f"{md4.multi(10, 30)}")


# for specific function as alias  # >> from modulename import fun1 as fn
from modle4 import factorial as fact 
fact(7) 


# for all function in module  # >> from modlename import *
from modle4 import *
factorial(3)
print(multi(3, 2))
print(swipe_function(1, 4))


