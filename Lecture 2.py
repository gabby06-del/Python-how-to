# =============================================================
# LECTURE 2: STRINGS, INPUT/OUTPUT, BRANCHING
# =============================================================


# =============================================================
# STRINGS
# =============================================================
# A str is a sequence of case-sensitive characters (letters,
# special characters, spaces, digits).
# Strings are enclosed in quotation marks or single quotes —
# just be consistent with which type you use in your code.
#
# You can concatenate and repeat strings.

# --- Example ---
a = 'me'
b = 'myself'
c = a + b           # 'memyself'
d = a + ' ' + b      # 'me myself'
silly = a * 3        # 'mememe'


# =============================================================
# STRING OPERATIONS
# =============================================================
# len() retrieves the length of a string.

# --- Slicing to get ONE character ---
# Square brackets perform indexing into a string to get the
# value at a certain position. In CS we always start at index 0.

# --- Example ---
s = 'abc'
s[1]     # 'b'
s[-1]    # 'c'  (negative index counts from the end)

# --- Slicing to get a SUBSTRING ---
# Syntax: s[start:stop:step]
# Gets characters from start up to (but NOT including) stop,
# taking every `step` character. If only [start:stop] is given,
# step defaults to 1.

# --- Example ---
s = 'abcdefgh'
s[3:6]    # 'def'      (starts at index 3, ends before index 6)
s[:]      # 'abcdefgh' (the whole string)
s[::-1]   # 'hgfedcba' (reversed)


# =============================================================
# IMMUTABLE STRINGS
# =============================================================
# Strings are immutable — they cannot be modified in place.
# You can only create NEW string objects (versions of the original).
# A variable name can only be bound to one object at a time.


# =============================================================
# PRINTING (OUTPUT)
# =============================================================
# print() outputs values to the console.
# Separate objects with commas to print them separated by spaces.
# Concatenate strings with + to print them as a single object.


# =============================================================
# INPUT
# =============================================================
# x = input(s)
#   -> prints the string s as a prompt
#   -> user types something and hits enter
#   -> that value is assigned to the variable x (always as a string)

# --- Example ---
# text = input("Type anything: ")
# print(5 * text)

# --- Example ---
# text = input("Give me a verb: ")
# print("I can", text, "better than you!")
# print((' ' + text) * 5)
#
# I can run better than you!
#  run run run run run


# =============================================================
# NEWTON'S METHOD
# =============================================================
# Goal: find the root of a polynomial — find g such that
#       f(g, x) = g**3 - x = 0
#
# Uses successive approximation:
#   next_guess = guess - (f(guess) / f'(guess))

# --- Example: Newton-Raphson for cube root ---
# x = int(input("What x to find the cube root of? "))
# g = int(input("What guess to start with? "))
# print("Current estimate cubed =", g**3)
# next_g = g - ((g**3 - x) / (3 * g**2))
# print("Next guess to try =", next_g)
#
# Current estimate cubed = 27
# Next guess to try = 3.2962962962962963


# =============================================================
# F-STRINGS
# =============================================================
# The character f before a string literal creates a formatted
# string. Expressions in curly braces {} are evaluated at
# runtime, automatically converted to strings, and inserted into
# the surrounding text. Anything outside {} is printed literally.

# --- Example ---
num = 3000
fraction = 1 / 3
print(f'{num * fraction} is {fraction * 100}% of {num}')
# 1000.0 is 33.33333333333333% of 3000


# =============================================================
# BINDING VS. EQUALITY
# =============================================================
# In CS there are two distinct notions of "equal":
#
#   variable = value
#       -> ASSIGNMENT: changes the stored value of `variable`.
#          Nothing to "solve" — the computer just performs the action.
#
#   some_expression == other_expression
#       -> EQUALITY TEST: no binding happens, just a comparison.
#          The whole expression evaluates to True or False.


# =============================================================
# COMPARISON OPERATORS
# =============================================================
# All comparisons evaluate to a Boolean (True or False).
#
#   i > j    -> greater than
#   i >= j   -> greater than or equal to
#   i < j    -> less than
#   i <= j   -> less than or equal to
#   i == j   -> equality test (True if i and j are the same)
#   i != j   -> inequality test (True if i and j are different)


# =============================================================
# BRANCHING IN PYTHON
# =============================================================
# INDENTATION MATTERS in all branching structures below.

# --- if ---
# if <condition>:
#     <code>
# <rest of program>
#
# Runs the if-block only when <condition> is True.

# --- if / else ---
# if <condition>:
#     <code>
# else:
#     <code>
# <rest of program>
#
# Runs the if-block when True, otherwise runs the else-block.
# Exactly one of the two will always run — never both, never neither.

# --- if / elif / elif ---
# if <condition>:
#     <code>
# elif <condition>:
#     <code>
# elif <condition>:
#     <code>
# <rest of program>
#
# Runs the FIRST block whose condition is True, then skips the rest
# — even if multiple conditions are True. It's possible none run.

# --- if / elif / else ---
# if <condition>:
#     <code>
# elif <condition>:
#     <code>
# else:
#     <code>
# <rest of program>
#
# Runs the first True block; if none are True, the else-block runs.


# =============================================================
# EXERCISE
# =============================================================
num = 4

if num == 0:
    print("The number is equal to zero")
elif num > 0:
    print("The number is positive")
else:
    print("Number is negative")