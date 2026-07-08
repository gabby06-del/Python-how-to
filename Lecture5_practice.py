# Lecture 5 Practice problem
# this problem is a bit more applicable to real life and goes over some areas where python may have some difficulties 

#PROBLEM:
##You're a junior programmer at a bank. A customer just called furious — their account shows $0.999999999999999 instead of $1.00, 
# and they want to know if the bank is stealing fractions of a penny from everyone. Your job: investigate whether floats are secretly 
# untrustworthy, and build a tool that won't get the bank sued.

## ------Practice instructions
# Your job: figure out whether floats can be trusted, and build tools that handle them safely.
##
## NOTE: the code below is a worked EXAMPLE/solution, not a template to fill in. Try writing your own version of each part BEFORE reading it, then use it to check your work.

## WHAT TO DO

## PART 1 - Crack the case
##   1. Take the decimal-to-binary conversion code from the lecture
##      notes (the one that converts x = 0.625) and run it on a few
##      different decimals: 0.5, 0.625, 0.25, and 0.1
##   2. For 0.1, the loop will hang and never finish - let it run, then
##      stop it yourself (Ctrl+C), and write down why you think that
##      happened.

## PART 2 - Add a cutoff
##   1. Add a maximum number of iterations (try 50) to the loop from
##      Part A so it can never hang forever.
##   2. Re-run it on 0.1. It should now print an approximate binary
##      value instead of hanging. Try changing the cutoff to 10, then
##      25, then 50, and see how the answer changes.

## PART 3 - Build the bank's rounding policy
##   1. Take the square root approximation code from the lecture notes
##      (the one that approximates the square root of 36).
##   2. Run it once on a perfect square (36) and once on a non-perfect
##      square (10). Compare the results.
##   3. Speed round: find the loosest epsilon/increment combo that still
##      gets within 0.01 of the true answer, using as few guesses as
##      possible.
##   4. Precision round: get as close as you can to the true square root
##      of 10 without your loop taking more than a few seconds to run.
##   5. Bug bounty: start from the version of the code WITHOUT the
##      guess**2 <= x overshoot protection. Find values of epsilon and
##      increment that make it overshoot or run for a very long time.
##      Then add the protection back in and confirm it now fails
##      gracefully instead of hanging.

## When you're done, compare your code to the example below.

## ---------- EXAMPLE ---------------

#PART 1: Binary Fraction Detector

x = 0.625
max_iterations = 50

p = 0
while ((2**p) * x) % 1 != 0:
    p += 1
    if p >= max_iterations:
        break 

num = int((2**p) * x)

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2

for i in range(p - len(result)):
    result = "0" + result

whole_part = result[0:-p]
if whole_part == '':
    whole_part = '0' 
result = whole_part + "." + result[-p:]

print(f"{x} -> {result}   (used {p} bits)")


x = 0.1
max_iterations = 50

p = 0
while ((2**p) * x) % 1 != 0:
    p += 1
    if p >= max_iterations:
        break

num = int((2**p) * x)

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2

for i in range(p - len(result)):
    result = "0" + result

whole_part = result[0:-p]
if whole_part == '':
    whole_part = '0'
result = whole_part + "." + result[-p:]

print(f"{x} -> {result}   (used {p} bits)")

#PART 2:  the cutoff is already built into Part 1 above (max_iterations + break)
## try changing max_iterations to 10, then 25, then 50 for x = 0.1 and see the
## approximation slowly get longer and closer, but never finish
 
#PART 3:  Approximate square root, gamified this reuses the approximation code straight from the lecture, with the overshoot protection already added in
x = 36
epsilon = 0.01
increment = 0.001
guess = 0.0
num_guess = 0

while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guess += 1

print(f"Speed round: {num_guess} guesses, guess = {guess}")


## --- Precision round
x = 10
epsilon = 0.0001
increment = 0.00001
guess = 0.0
num_guess = 0

while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guess += 1

print(f"Precision round: {num_guess} guesses, guess = {guess}")
print(f"(actual square root of {x} is approximately 3.16227766)")


## --- Bug bounty:

x = 10
epsilon = 0.0001
increment = 0.01
guess = 0.0
num_guess = 0
max_guesses = 100000  
while abs(guess**2 - x) >= epsilon:
    guess += increment
    num_guess += 1
    if num_guess >= max_guesses:
        break

print(f"Unprotected version: after {num_guess} guesses, guess = {guess}")
print("It never satisfied epsilon on its own - it just kept climbing until we force-stopped it.")



x = 10
epsilon = 0.0001
increment = 0.01
guess = 0.0
num_guess = 0

while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guess += 1

print(f"Protected version: after {num_guess} guesses, guess = {guess}")
if abs(guess**2 - x) >= epsilon:
    print(f"Failed on sqrt of {x}")
else:
    print(f"{guess} is close to square root of {x}")

