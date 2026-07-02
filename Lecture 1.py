## Programs manipulate data objects 
#objects have a type that defines the kinds of things programs can do to them
# 30 
# - is a number 
# - we can add/sub/multiply/div/exo
# 'ana'
# is a sequence of characters (aka a string)
# we can grab substrings, but we can't divide it by a number (how long/what character is at a certain position)

# scalar objects (cannot be subdivided) - numbers, truth values
# non-scalar (have internal structure that can be assessed) - lists, dictionaries, sequence of characters

#scalar object types:
# int - represents integers, e.g. 5, -100
# float - represents real numbers, e.g. 3.25, 2.0 
# bool - represents Boolean values True and False
# NoneType - special and has one value, None
# can use type() to see the type of an object

#type conversions (casting) - can convert object of one type to another 
# float (3) casts the int 3 to float 3.0
# int(3.9) casts the float 3.9 to int 3

#combine objects and operators to form expressions
# 3+2 or 5/3

#an expression has a value which has a type 
#python evaluates expressions and stores the value, it doesnt store expressions
#syntax for simple expression <object><operator><object>

## >>> type(5)
# <class 'int'>
# >>> float(3)
# 3.0
# >>> int(4.9)
# 4
# >>> round(5.8)
# 6
# >>> type(float(123))
# <class 'float'>
# >>> 5*5
# 25
#
# >>> type (3*2)
# <class 'i

## computations go left to right like in math
# do computations inside parens first 


##Operators on int and float 
# i+J the sum
# i-j the difference
# i*j the product 
# --------- for above if both are ints the result is int, if either or both are floats, result is float (truth table logic)----

# i/j division ---- result is always a float 
# i//j floor division 
# i%j the remainder when i is divided by j
# i**j i to the power of j
#---- e.g.----
##>>> 5/3
# 1.6666666666666667
# >>> 5//3
# 1
# >>> 5%3
# 2
# >>> 5**3
# 125
#--------

## Variables 
# Math variables are abstract and can represent many values -- e.g. x represents all square roots
# CS variables is bound to one single value at a given time, can be bound to an expression (but expressions evaluate to one value)

## Binding variables to values 
# In CS the equal sign is an assignment: one value to one variable name, equal sign is not equality 
# An assignment binds a value to a name 

## STEP 1: Compute the value on the RHS (the VALUE) -- value stroed in computer memory 
## STEP 2: Store it (bind it) to the LHS (the VARIABLE) -- retrieve value associated with name by invoking the name (typing it out)
# e.g. pi=3.14159

## Abstracting expressions
# We give names to values of expressions to reuse names instead of values and to make code easier to read and modify 
# Variable names must be chosen wisely-- code needs to be readable and make sense to you and others, it'll be ok if you stick to letters, underscores, dont start with a number 

# e.g. Compute approximate value for pi 
# pi = 355/113
# radius = 2.2
# area = pi * (radius**2)
# circ = pi * (radius*2)

# ---------

## Change bindings 
# we can change variable names and bind it to a completely different value, previous value may still be stored in memory but lost the handle for it 
# e.g.
# pi = 3.14
# radius = 2.2 
# area = pi * (radius**2)
# radius = radius+1
# -- in this case the value for area does not change until you let the computer do the calculation again ---
# -- lines are excecuted in succession ---

# e.g. swap values of x and y without binding the numbers directly 
# x= 1
# y= 2
# temp = y
# --
# y=x
# x=temp 


## Exercise: Assume 3 variables are already defined for you: a, b, and c. Create a variable called total that adds a and b then multiplies the result by c. Include a last line in your code to print the value: print(total)

a=1 
b=2 
c= 3

total = (a+b)*c
print(total)