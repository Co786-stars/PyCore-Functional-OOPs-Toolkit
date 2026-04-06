# Definition:
# map() takes a function and one or more iterables, applies the function to each element,
# and produces a map object (iterator). Converting it to list/tuple shows the results.

# Syntax:
# map(function, iterable1, iterable2, ...)

m = ['1', '2', '3', '4']
t = map(int, m)   # map() applies int() to each element of m
print(list(t), list(m))
'''
Step 1: When Python reads line (t = map(int, m)),
        it does not immediately convert the strings.
        It only creates a map object (an iterator) that knows
        how to apply int() to each element of m later.

Step 2: When Python reaches line (print(list(t), list(m))),
        it now starts consuming the map object.

Step 3: At this moment, Python goes back to line (t = map(int,m)) 
        internally and applies int() to the first element of m:
        '1' → 1. Then it continues for each element:
        '2' → 2, '3' → 3, '4' → 4.

Step 4: After converting all elements, list(t) becomes [1, 2, 3, 4].

Step 5: The original list m is unchanged, so list(m) still shows ['1', '2', '3', '4'].

Note : - 
line 9th only sets up the map object, and line 10th is where the actual conversion 
happens, one element at a time, before printing.
'''


def func(num):
    return len(num)   # func() takes a string and returns its length

var = ('word', 'wait', 'wizard')   # tuple of strings
t = map(func, var)   # map() sets up an iterator to apply func() to each element of var
print(list(t))       # consuming the map object to see results
'''
Step 1: → Python defines func(num), which returns the length of a string.
Step 2: → var is a tuple ('word', 'wait', 'wizard').
Step 3: → t = map(func, var). No function calls yet, only a map object created.
Step 4: → print(list(t)) starts consuming the map object.
          Internally Python calls func() one by one:
            func('word')   → len('word')   → 4 → list becomes [4]
            func('wait')   → len('wait')   → 4 → list becomes [4, 4]
            func('wizard') → len('wizard') → 6 → list becomes [4, 4, 6]
Step 5: → Finally, list(t) = [4, 4, 6] is printed.
'''



# Definition :-
# - A lambda function is an anonymous function (no name) defined with the keyword lambda.
# - It can take any number of arguments but must have only one expression.
# - The result of that expression is automatically returned.

# Syntax :-
# lambda arguments: expression

# Note : -
# A lambda function is just a quick way to write a function inline, often used when you don’t
# want to define a full def function.


f = lambda x, y: x + y
print(f(3, 2)) # output:5
'''
Explanation:
→ f is defined as a lambda function.
    It takes two arguments (x, y) and returns their sum (x + y).

→ When we call f(3, 2):
     Internally Python substitutes x = 3, y = 2
     → evaluates 3 + 2
     → returns 5
  f(x, y) simply returns x + y.
  
→ Manual way: -
   def f(x, y):
     return x + y
'''


lst = ['4', '3', '2', '1']
f = map(lambda arg: int(arg), lst)
print(list(f))
'''
→ Manual way : -
def f(arg):
    return int(arg)   # convert each string to int

lst = ['4', '3', '2', '1']
t = map(f, lst)       # now f is applied to each element
print(list(t))        # Output: [4, 3, 2, 1]
'''

