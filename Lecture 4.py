## Lecture 4: Guess and check algorithm, binary, and fractions

#  BREAK STATEMENT
# Immediately exits whatever loop it is in and skips the remaining expressions in that code block.
# break only exits the innermost loop it is directly inside of.
# code structure:
# while <condition_1>:
#    while <condition_2>:
#       <expression_a>
#       break
#       <expression_b>
#    <expression_c>

# expression_a runs whenever condition_1 and condition_2 both hold (both True)
# because of the break, expression_b will never run - the loop exits as soon as break is hit (this is why the example above is "bad code": expression_b is dead code)
# expression_c runs each time the inner while loop finishes (including when it exits early via break), as long as condition_1 is still true
# break exists so we can exit a loop early, before its condition naturally becomes False

## STRINGS AND LOOPS
# e.g. finding the number of "o"s or "a"s in a sentence
# this code uses range() to iterate through the indices of s
s = "demo loop: an apple a day keeps the doctor away"
for index in range(len(s)):
    if s[index] == "o" or s[index] == "a":
        print("there is an o or a")
# there is an o or a *11

# we can write this in simpler ways

for char in s:
    if char == "i" or char == "o":
        print("there is an i or o")

# we can also write it like this (iterates through the characters of s directly - most pythonic)

for char in s:
    if char in "ap":
        print("there is an a or p")

# the sequence of values in a for loop isn't restricted to numbers - it can also be a string (or any sequence)

# e.g. count how many unique letters there are in the string
s = "how many letters"
seen = ""
for w in s:
    if w not in seen:
        seen = seen + w
print(len(seen))

## now that we have these building blocks, we can start writing real code - but there are also ways to improve our code's readability and efficiency

# GUESS AND CHECK ALGORITHM
# a basic algorithm to start with is the guess and check algorithm
# this algorithm uses a process called exhaustive enumeration: we guess a value for the solution, then test whether that value actually answers our problem
# we keep guessing until the answer is found, or until all possible answers are exhausted and no viable answer is found

# e.g. find the square root of a perfect square
# the main idea: given an integer, we want to see if there is another integer that is its square root. Start with a guess and check whether it fits. Guessing should not be random - it should be systematic.
# we could guess every number one by one, but it's better to add some algebraic reasoning: if guess squared is already bigger than the number we're checking, we can stop - no need to keep guessing higher

i = int(input("enter an integer: "))
guess = 0
while (guess**2) < i:
    guess += 1
if (guess**2) == i:
    print(f"the square root is {guess}")
if (guess**2) > i:
    print(f"there is no perfect square for {i} ")

# written out step by step on purpose, to make it clear how guess and check works
# to handle negative inputs, we can add an extra precaution by flagging negative values
i = int(input("enter an integer: "))
guess = 0
neg_int = False
if i < 0:
    neg_int = True
while (guess**2) < i:
    guess += 1
if (guess**2) == i:
    print(f"the square root is {guess}")
if (guess**2) > i:
    print(f"there is no perfect square for {i} ")
    if neg_int:
        print(" Did you maybe mean", -i, "?")

# an important thing to note about guess and check algorithms: they cannot run indefinitely and must have a stopping point
# a good use for this type of algorithm is checking for a secret number, or building something like a password checker
# example: finding a secret number

secret_num = 8
found = False
guess = 0

for guess in range(0, 10):
    if guess == secret_num:
        print(f"Secret number is {guess}")
        found = True
if not found:
    print("Secret number not found")

# we're using found as a Boolean flag here - it's not a special type, just a regular variable, but flags like this are a useful pattern for tracking whether an event happened
# code tends to look cleaner when you iterate directly over a sequence of values (using a for loop) rather than managing an index/counter by hand
# for loops also tend to introduce fewer bugs and are generally easier to use than while loops

# another use for guess and check algorithms is solving word problems: assign all known values, write out the relationships as equations/conditions, and let the computer guess and check which combination of values satisfies them all
# e.g. Taylor, Brad, and Athena all go to a hackathon. Taylor does 2 hours of work, Brad does twice as much work as Athena, and there were 20 hours of work done in total. How much work did Athena do?

hours_worked_total = 20
for athena in range(21):
    for taylor in range(21):
        for brad in range(21):
            hours_committed = (taylor + brad + athena == 20)
            taylor_worked_two = (taylor == 2)
            brad_double_athena = (brad == 2 * athena)
            if hours_committed and taylor_worked_two and brad_double_athena:
                print(f"Athena worked {athena} hours")
                print(f"Brad worked {brad} hours")
                print(f"Taylor worked {taylor} hours")

## now that we understand this computational/mathematical logic, we can look at binary

## BINARY NUMBERS
# so far, numbers in Python have been expressed as int (integers) or float (real/decimal numbers)
# keep in mind: operations on floats can introduce a very small rounding error, and this error can compound and become significant over many operations
# this error exists because floats are only an approximation of real numbers inside a computer. That disconnect comes from the fact that humans naturally think in base 10, while computers represent everything in base 2, as a sequence of bits (0s and 1s)
# this mismatch between human and computer number systems affects how we need to think about and write code (a bit like something getting lost in translation between two languages)
# computers use base 2 because it's easy to implement in hardware - it's simple to build components that reliably sit in one of two states. Computers are built around storing information and doing arithmetic using just 0s and 1s. This is similar in spirit to spin-up/spin-down states of particles in quantum mechanics.

# converting integers to binary is straightforward - we can easily transform a base-10 number into base-2

# the base-10 representation of an integer is a sum of powers of 10, each scaled by a digit from 0 to 9
# e.g. 1230 = 1*10**3 + 2*10**2 + 3*10**1 + 0*10**0

# binary representation is the same idea, but in base 2: a sum of powers of 2, each scaled by a digit that is either 0 or 1
# e.g.
# 1230 = 1*2**10 + 1*2**7 + 1*2**6 + 1*2**3 + 1*2**2 + 1*2**1
#      = 1024 + 128 + 64 + 8 + 4 + 2
#      = 1230
#      = 10011001110 (base 2)

# working this out by hand this way is very tedious
# a more systematic method: take the remainder of the number divided by 2 - that gives you the last (rightmost) binary bit. Then integer-divide the number by 2, which shifts everything over by one bit.
# repeat these successive divisions (each remainder becomes the next bit, read right to left) until the number reaches 0

num = 1230
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
print(result)
# 10011001110