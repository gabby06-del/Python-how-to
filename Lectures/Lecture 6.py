## Lecture 6: Bisection search algorithm and Newton-Raphson 
#  
# Bisection search differs from Guess and cChecks as it does not guess counting each number one by one but cuts the set of whatever is being guess in half at each section 
# the process of cutting the set of things in half at each stage is characteristic of logarithmic growth 

## The main difference between the guess and check algorithm and the bisection search algorithm is that by guessing the halfway point is logarithmic on the number 
#of possible guesses (bisection search) which is much more efficient than checking each number one by one iteratively 

## Bisection search for square root
# Keeping the same question as before for other algorithms we will be trying to find the approximation of the square root using bisection search 
# if we know the answer lies in between 0 and x instead of starting at 0 we pick a number within the selected range at the middle point 
# if this guess is not close enough to the wanted number then one must ask if the guess is too big or too small
# if g**2 > x then g is too big so nthe next guess must fall within the lower half of range 
# one must repeat this process until value is found 

# bisection search takes advantage of properties of the problem and has two main properties which must be satisfied in order to utilize the algorithm:
# - There is some ordering to the thing being searched
# - We can tell whether the guess was too high or too low

# now that we know the reasoning behind finding the square root using bisection search we can look at the code:

x = 12345
epsilon = 0.01
num_guess= 0
low=0
high= x
guess = (high+low)/2.0
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess**2
    else: 
        high = guess
    guess = (high + low)/2.0
    num_guess+=1

print(f"num_guesses= {num_guess}")
print(f"{guess} is close to square root of {x}")

# if this code is run it is seen to be a lot more efficient than the guess and check algorithm which is brute forcing the guesses
# doing the one by one guess approach is linear in size of problem because number to steps grows linearly as we increase problem size
# bisection search is logarithmic in size of problem as number of steps grows logarithmically with problem size

# search space
# - 1st guess: N/2
# - 2nd guess: N/4
# - Kth guess: N/2**k
# k = log(N)

# however with the current code above it cannot compute the square root of 0.5 as it gets stuck in an infinite loop 
# to fix this issue the code should be written as 

x = 0.5
epsilon = 0.01
if x>=1:
    low = 1.0
    high= x
else: 
    low = x
    high = 1.0

guess = (high+low)/2.0
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess**2
    else: 
        high = guess
    guess = (high + low)/2.0
    num_guess+=1

print(f"num_guesses= {num_guess}")
print(f"{guess} is close to square root of {x}")

# some things can be seen when doing bisection search. It reduces computation time, and the search space gets smaller quickly at the beginning but the rate of change decreases as the search space gets smaller


## Newton-Raphson 
# this algorithm is the general approximation algorithm to find roots of a polynomial in one variable 
# (using _/ to denote subscript)
# -- p(x) = a_/n x**nm + a_/n-1 x**n-1 + ... + a_/1 x + a_/0
# Newton and Raphson showed that if g is an approximation to the root then g - p(g)/p'(g) is a better approximation 

# using this logic we can find the root using the newton raphson algorithm 
# simple case for a polynomial: x**2 - k 
# derivative = 2x
# given guess after another guess: g - (g**2 - k)/2g
# using these steps we can eventually find the approximation to the square root of k!

epsilon = 0.01
k = 24.0 
guess = k/2.0 
num_guesses = 0
while abs(guess*guess - k) >epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - k)/(2*guess))

print(f"num_guesses= {str(num_guesses)}")
print(f"srt of {str(k) is about {str(guess)}}")

## a fun thing to note is that every algorithm used/learned thus far is an iterative algorithm 

