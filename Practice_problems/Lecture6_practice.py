# LECTURE 6 PRACTICE SET
# for this practice set there are three parts:
# 1. Bisection search - write a function bisection_cube_root(x,epsilon) that finds the cube root of x using bisection search 
# 2. Newton-Raphson - write a function newton_r_cuberoot(k, epsilon) that finds the cube root of K using Newton-Raphson
# 3. Theory - Run both functions on x = 1000000 (one million) and compare num_guesses. Which one wins, and why does that match what the lecture said about logarithmic vs. other growth rates?

# ----- STARTER CODE -----
# since this is pretty generic knowledge for computer science I am providing a barebones starter code so that you may be able to complete the logic and run the code according to what is listed in the practice set instructions

def bisection_cube_root(x, epsilon):
    num_guesses = 0
    # TODO: set up low and high correctly for both cases (x >= 1 and 0 < x < 1)
    
    # TODO: initialize guess
    
    while abs(guess**3 - x) >= epsilon:
        # TODO: narrow the search space
        # TODO: update guess
        # TODO: increment num_guesses
        break
    
    return guess, num_guesses

print(bisection_cube_root(27, 0.01))   # should be close to 3
print(bisection_cube_root(0.125, 0.01))  # should be close to 0.5

def newton_r_cuberoot(k, epsilon):
    guess = k / 2.0
    num_guesses = 0
    # TODO: implement the Newton-Raphson loop
    
    return guess, num_guesses

print(newton_r_cuberoot(27, 0.01))



