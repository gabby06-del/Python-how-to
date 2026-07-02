## Lecture 2: Strings, Input/Output, Branching

## Strings 
# A str is a sequence of case sensitive characters (letters, special char, spaces, dig)
# They are enclosed in quotation marks or single quotes (important to be consistent of the type used in code)
# concactenate and repeat strings 

# ---- e.g. ----
# a = 'me'
# b= 'myself'
# c = a+b --- (memyself)
# d = a + ' ' + b  ---- (me myself)
# silly = a * 3 ---- (mememe)

## String operation 
# len () is a function to retrive the length of a string in parentheses

## Slicing to get one character in a string 
# square brackets used to perform indexing into a string to get the value at a certain index/position 

#- e.g. - 
# s= 'abc'
# s[1]
# b
# in CS we always start at 0 

# s [-1]
# c 

## Slicing to get a substring
# can slice using strings using [start:stop:step]
# get characters at start, up to and including stop, taking every step character
# if give two numbers, [start:stop], step=1 by default 

# e.g 
# s = 'abcdefgh'
# s[3:6] -- evaluates to 'def' starts at 3 and ends at 6
# s[:] -- abcdefgh
# s[::-1] -- evaluates to 'hgfedcba'

#---------

## Immutable Strings 
# strings are immutable - cannot be modified 
# you can create new objects that are versions of the original one
#  variable name can only be bound to one object

## Printing (output)
# used to output stuff to console, the command is print()
# seperate objects using commas to output them seperated by spaces 
# concatenate strings together by using + to print as a single object


## Input
# x= input(s) 
# prints the value of the string s 
# user types smth and hits enter, that value is assigned to the bariable x
# text = input("Type anything: ")
# print (5*text)

#-- e.g--
#text = input("give me a verb:")
# print("I can", text, "better than you!")
# print((' '+text)*5)
# I can run better than you!
#  run run run run run


## Newton's Method 
#want to find roots of a polynomial: find g such that f(g,x)=g**3-x=0
#algorithm uses successive approximation: next_guess= guess - (f(guess)/f'(guess))
#-- e.g. Newton's Raphson for cube root--
# x = int(input("What x to find the cube root of? "))
# g = int(input("What guess to start with? "))
# print("current estimate cubed= ", g**3)
# next_g = g - ((g**3 - x) / (3*g**2))
# print("Next guess to try =  ", next_g)
#current estimate cubed=  27
# Next guess to try =   3.2962962962962963

## F-strings
#character f followed by a formatted string literal 
#anything that can appear in a normal string literal, expressions bracketed by curly braces 
# expression in curly braces evaluated at runtime, automatically converted to strings, and concatenated to the string preceding them 
# allows us to not think about printing and expressions, so anything that is not in a culry bracket is printed literally and what is in a culry bracket is an expression 

## e.g.
# num= 3000
# fraction = 1/3 
# print( f'{num*fraction} is {fraction*100}% of {num}')
# 1000.0 is 33.33333333333333% of 3000
#instead of having to do it all individually 

## Binding variables and values 
# in CS there are two notions of equal - assignment and equality test 
# variable = value -> change the stored value of variable to value, nothing to solve computer just does the action 
# some_expression == other_expression -> A test for equality, no binding is happening, just doing a comparison and replacing the entire line with True or False

## Comparison operators
# i and j are variable names, comparisons below evaluate to the type Boolean (true or false)
# i>j 
# i>= j
# i < j
# i<= j
# i == j -> equality test, True if i is the same as j
# i!= j -> inequality test, True if i is not the same as j

## Branching in Python 
# if <condition>:
#     <code>
#     <code>
# <rest of program>

# <condition> has a value of true or false 
# do code within if block if condition is true
# INDENTATION MATTERS

# if <condition>:
#     <code>
#     <code>
# else: 
#     <code>
#     <code>
# <rest of program>

# <condition> has a value of true or false 
# do code within if block if condition is true or code within else block will run when condition is false 
# will never skip both and will never do both 

# if <condition>:
#     <code>
#     <code>
# elif: 
#     <code>
#     <code>
# elif: 
#     <code>
#     <code>
# <rest of program>

# <condition> has a value of true or false 
# do code within if block if condition is true or excecute the code within elif (elseif) or another elif until it joins the rest of the program 
# the first elif that runs is the only one that will be exceuted even if multiple are true 
# only one elif can run however it is possible that none run 

# if <condition>:
#     <code>
#     <code>
# elif: 
#     <code>
#     <code>
# else: 
#     <code>
#     <code>
# <rest of program>

# <condition> has a value of true or false 
# do code within if block if condition is true. The else block runs if no conditions were True


# exercise
# num = 4
# if num == 0: 
#   print("The number is equal to zero")
# elif num > 0: 
#   print("The number is positive")
# else:
#   print("Number is negative")