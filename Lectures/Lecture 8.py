##LECTURE 8: FUNCTIONS CONTINUED 

# in the last lecture we were looking into functions and how a function must always return something 
# However, what happens if there is no return command. If this happens then python returns the value None, if there is no return give 
# It represents the abscence of a value and nothing is printed and it is essentially null in whatever code it is being used in 

# if we were to write this out explicitly (using the example from the last lecture) it would look like the following:

def is_even( i ): 
    """
    Docstring for is_even
    
    :param i: Description
    """
    i%2 == 0
    return None 

# the return None is never actually written explicitly and is added in by python 
# None is a value of type NoneType and is the abscence of a value 

# while return and print seem to have similar properties and similar actions we should look at the difference between the two

## RETURN
# return only has meaning inside a function and only one return can be excecuted inside a function 
# cude can lie inside of a function but after the retrun statement the rest of the code is not excecuted acting much like a break 
# the return function also has a value associated with it, which is then given to function caller 

## PRINT
# print can be used in and outside of function and one can excecute many print statements inside a function 
# code inside a function can be excecuted after a print statement and the value associated with it is outputted to the console 
# the print expression itself returns None value 

## FUNCTIONS IN LARGER PIECES OF CODE

# functions are very useful in larger pieces of code because if debugged it does not introduce a source of error and it makes code readable
# we can see this by looking at our bisection root finder and turning it into a function 

def bisection_root(x):
    """
    Docstring for bisection_root
    
    :param x: Description
    """
    epsilon = 0.01
    low = 0 
    high = x
    ans = (high + low)/2.0 
    while abs(ans**2-x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans 
        ans = (high + low)/2.0 
    return ans

# we can then call this function with any number as x and it will return the root closest to x 
# for example
print(bisection_root(5))
#we didnt need to know how this function works to be able to call it 

#this also shows us how functions support modularity and clean up our code when writing it making it easier to debug 
# in the instance we were writing a whole code instead of writing it explicitly we could do:

print("This is a root finder using bisection search")
x = (float(input("What number do you want to find the root of?: ")))

result=bisection_root(x)

print(f"The square root of {x} is approximately {result}")



## What happens every time a function is called?
# python creates a new environment with every function call, it basically runs a mini program every time and this program runs with assigning its parameters to some inputs 
# once the work has been done and the function returns a value the environment dissapears leaving just the value

## ENVIRONMENTS

# when a program is first run it enters a global environment the main environment that the program sits in 
# a global environemtn is where the user interacts with the python interpretes and where the program starts out 
# calling or invoking a function creates a new environment
# while the new environment branches off of the old one they don't interfere with each other or interact very much they only interact when passing in parameters and returning associated values 
# this means that each environment can have functions or variables with the same name and different assigned values without interfeering with each other (e.g. overwriting each other), they are basically completely new coding spaces 

#e.g. 

def f(x):
    x = x+1
    print(f"in f(x): x={x}")
    return x
# everything before this is the function definition 
x=2
z=f(x)

# the two parameters above are the actual parameters and are the main program code 
# so inside a function can access a variable defined outside but inside a function cannot modify a variable defined outside (it is possible by using global variables but should not be done)

## HIGHER ORDER PROCEDURES

# objects in Python have a type like we've seen before (int, float, Nonetype) and can appear in RHS of assignment statement 
# objects can be used as an argument to and can be returned as a value from a procedure 
# functions are also objects so they act the same as any other object discussed previously 

