
"""

A collection of simple math operations


Functions
---------
simple_add : Add two numbers
simple_sub : Subtract two numbers
simple_mult : Multiply two numbers
simple_div : Divide two numbers
poly_first : Evaluate a first-order polynomial
poly_second : Evaluate a second-order polynomial


Parameters
------------
object：float or int


Returns
------------
result: float or int


Example
------------
>>>simple_math.simple_add(1,2)
3


"""

def simple_add(a,b):
    return a+b

def simple_sub(a,b):
    return a-b

def simple_mult(a,b):
    return a*b

def simple_div(a,b):
    return a/b

def poly_first(x, a0, a1):
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....
