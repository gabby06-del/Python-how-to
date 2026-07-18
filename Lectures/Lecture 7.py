## LECTURE 7: Functions: Decomposition, abstraction, specifications
# Abstractions in an Object-Oriented Programing language (OOP) gives us an abstraction that hides the internal details in implementations
# Through this we just need to know which methods of the object are available to call and which input parameters are needed to trigger a specific operation 
# Through abstraction we dont need to know or understand how this method is implemented and which kinds of actions it has to perform to carry out an expected result 

# Types of OOP languages:
# - Python 
# - Java 
# - C++
# - Javascript 

#There are different types of abstraction but there are two primary ones: data abstraction and process abstraction 
# Data abstraction abstracts data identities and process abstraction hides the underlying implementation of a process

# In coding we want to be able to write and debug a piece of code for regular use without needing to know or understand the logic behind it and just be able to use, which is exactly what abstraction is
# In coding one achieves abstraction with a function. A function lets us create a placeholder where once we create that function it will produce an output from inputs while hiding the details on how it achieves such outputs
# We have already been using functions throughout these lectures, like abs() and len(). We don't know what process it performs but we know what the use is and what the output will be 

# The idea behind a function is we want to abstract away (conceal) how that functions achieves something
# To do this we will create a function and note down what this function does using docstrings
# Docstrings are essentially a point of communication between the creator of the function and those who want to use it and acts as a how-to manual. 
# in this manual (contract) we will find/write: what the inputs to the function are, what is the function doing?, what is the output of the function?

# Given this idea of abstraction we must break these functions apart into modules that are self contained and reusable. 
# A modules role is to break up code into logical pieces, keep code organized, and keep it readable for those reusing it 
# All of this goes back to the idea of decomposition which is breaking apart functions and code into reproducible lines of code. Decomposition relies on abstraction to ease the construction of complex modules from simple code

## Functions 
# functions as mentioned before are reusable pieces of code which capture steps of a computation so that we can use with any corresponding input 
# functions are nothing special they are very similar to the code that we have been writing but in a clearer format for reproducibility 
# To use functions we must define a function, defining a function tells Python that there is now some code residing in its memory which can be used for some process
# when we define functions and write this code we are not running it but we are setting it aside
# functions are only useful when they are run in coding this is referred to as calling a function or invoking a function 
# once we write a function we can call it however many times we want to reuse the same block of code

# Function Characteristics
# For every function we wrtie it has a few things it must include:
# - Name : kind of like a variable bound to a function object
# - Formal parameters : inputs 
# - Docstring : a specification for the function, telling the user about input and output
# - Body : instructions to execute when function is called 
# - Returns something : keyword return

## HOW TO WRITE A FUNCTION 

def is_even (i): #def is keyword and is_even is the name (to callback), ( i ) are parameters or arguments 
    """ ## specifications, docstring
    Input: i, a positive int 
    Returns True if i is even, otherwise False
    """
    if i%2 == 0: # body 
        return True 
    else:
        return False  #return keyword tells us give back a value
    
## RATIONALE BEHIND WRITING A FUNCTION 
# what is the problem?
# how to solve the problem?
# can you make the code cleaner?

# to call the function written above we can write 

is_even(8)

# when we make this call python replaces formal parameters in the function definition with values from the function call
# in the case of is_even i is replaced with 3 
# python executes expressions in the body of the function 

# Inserting functions in code:
print("Numbers between 1 and 10: are they even or odd?")

for i in range(1,10): 
    if is_even(i):
        print(i, "even")
    else: 
        print(i, "odd")

# the main idea behind this is write code to solve a simple small problem so it can then be used within more complicated code