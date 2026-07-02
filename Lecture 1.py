# =============================================================
# OBJECTS IN PYTHON
# =============================================================
# Programs manipulate data objects.
# Objects have a type that defines what a program can do to them.
#
#   30    -> a number; supports +, -, *, /, **, etc.
#   'ana' -> a sequence of characters (a string); supports substring
#            operations (length, indexing), but NOT division by a number.

# --- Scalar vs. Non-scalar ---
# Scalar objects (cannot be subdivided): numbers, truth values
# Non-scalar objects (have internal structure): lists, dictionaries,
#                                                 strings

# --- Scalar object types ---
# int      -> integers, e.g. 5, -100
# float    -> real numbers, e.g. 3.25, 2.0
# bool     -> True / False
# NoneType -> special type with one value: None
#
# Use type() to check an object's type.


# =============================================================
# TYPE CONVERSION (CASTING)
# =============================================================
# You can convert an object of one type to another.
#   float(3)   -> 3.0   (int -> float)
#   int(3.9)   -> 3     (float -> int, truncates)

# --- Examples ---
# >>> type(5)
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
# >>> type(3*2)
# <class 'int'>


# =============================================================
# EXPRESSIONS
# =============================================================
# Combine objects and operators to form expressions, e.g. 3+2 or 5/3
#
# An expression has a value, and that value has a type.
# Python evaluates expressions and stores the VALUE — not the expression.
#
# Basic syntax: <object> <operator> <object>
#
# Order of operations follows standard math rules:
# computations go left to right, and parentheses are evaluated first.


# =============================================================
# OPERATORS ON int AND float
# =============================================================
#   i + j   -> sum
#   i - j   -> difference
#   i * j   -> product
#       (if both operands are int, result is int;
#        if either is float, result is float)
#
#   i / j   -> division        (always returns a float)
#   i // j  -> floor division
#   i % j   -> remainder (modulo)
#   i ** j  -> i to the power of j

# --- Examples ---
# >>> 5/3
# 1.6666666666666667
# >>> 5//3
# 1
# >>> 5%3
# 2
# >>> 5**3
# 125


# =============================================================
# VARIABLES
# =============================================================
# Math variables are abstract and can represent many values
#   (e.g. x can represent all square roots).
#
# CS variables are bound to ONE single value at a given time.
# A variable can be bound to an expression, but expressions always
# evaluate down to a single value before binding.

# --- Binding variables to values ---
# In CS, "=" is an ASSIGNMENT, not equality.
# An assignment binds a value to a name.
#
#   STEP 1: Compute the value on the RHS (stored in memory)
#   STEP 2: Bind that value to the name on the LHS
#           (retrieve it later just by typing the name)
#
#   e.g. pi = 3.14159


# =============================================================
# ABSTRACTING EXPRESSIONS
# =============================================================
# We name expressions so we can reuse the name instead of
# repeating the value — this also makes code more readable.
#
# Naming rules: use letters/underscores, don't start with a number,
# and pick names that are meaningful to you and others.

# --- Example: approximate value of pi ---
pi = 355 / 113
radius = 2.2
area = pi * (radius ** 2)
circ = pi * (radius * 2)


# =============================================================
# CHANGING BINDINGS
# =============================================================
# A variable name can be rebound to a completely different value.
# The old value may still exist in memory, but you lose the
# "handle" (name) to access it.
#
# Lines execute in succession — reassigning one variable does NOT
# automatically recompute anything that depended on its old value.

# --- Example ---
pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
radius = radius + 1
# area is still based on the OLD radius until recalculated!

# --- Example: swap x and y without hardcoding values ---
x = 1
y = 2
temp = y
y = x
x = temp


# =============================================================
# EXERCISE
# =============================================================
# Create `total` = (a + b) * c, then print it.

a = 1
b = 2
c = 3

total = (a + b) * c
print(total)