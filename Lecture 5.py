## LECTURE 5: Looking at floats in binary and working on more basic algorithms

## FRACTIONS IN BINARY
# for binary representation we use the idea a*2**-1 + b*2**-2 + c*2**-3 and so on
# this means that the binary representation of a decimal fraction f requires finding the values of a, b, c, etc. such that f = 0.5a + 0.25b + 0.125c + 0.0625d and so on
# to find this representation, the idea is: find a power of 2 big enough to turn f into a whole number, convert that whole number to binary, then divide by the same power of 2 (i.e. shift the decimal point) to restore the original value
# if there is no integer p such that x*(2**p) is a whole number, then the binary representation is always an approximation - but for this example we are assuming the decimal fraction has an exact binary representation, not an approximation
# so this conversion works precisely in some cases but not others: it depends on whether there exists a power of 2 that turns x into a whole number

# e.g.

x = 0.625
p = 0
while ((2**p) * x) % 1 != 0:  # checks whether there's still a decimal part left
    print("remainder= " + str((2**p) * x - int((2**p) * x)))
    p += 1
# this loop finds the power of 2 needed to make x a whole number
num = int((2**p) * x)  # converts x*(2**p) to an integer

result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
# this converts num to its binary representation

for i in range(p - len(result)):
    result = "0" + result
# pad the front with zeros so there are enough digits to place the decimal point correctly

result = result[0:-p] + "." + result[-p:]  # insert the decimal point in the correct place
print(f"The binary representation of the decimal {str(x)} is {str(result)}")

# this shows that converting fractions to binary by hand is a long, tedious process, but ultimately everything is represented in terms of bits
# real numbers are harder to represent and often cause problems, because we sometimes have to approximate what would otherwise be an infinite sequence of binary bits

## STORING FLOATING POINT NUMBERS
# a floating point number is stored as a pair of integers: a significant digit (the "significand"/mantissa) and a base-2 exponent

# e.g. (1, 1) - here the first 1 is the significant digit and the second 1 is the base-2 exponent
# (1, 1) represents 1 * 2**1
# 1 * 2**1 = 10 (base 2)
# = 2.0

# we care about this because we want to understand the error in our programs and why it happens
# it happens because computers only have a limited amount of space to store data
# most modern computers only have 32-64 bits of storage to represent significant digits
# if a number would require more than 32-64 bits to represent exactly in binary, the computer can't store all of that information, so the number gets rounded
# because of errors like this, we should never use == to test whether two floats are equal - instead we test whether they're within a small range (epsilon) of each other
# for the same reason, we need to be careful whenever we design code in Python that relies on floats

# we can build this knowledge into our guess and check algorithm to make it more accurate, using something called the approximation algorithm
# this is better than plain guess and check because it lets us find an approximate answer, rather than only telling us whether an exact answer was found or not
# the approximation algorithm isn't meant to give an exact answer - it gives an answer that is "close enough," which is where the name comes from

## APPROXIMATION

# for approximation, we want to find an answer that is good enough (within a certain distance of the real answer)
# to do this, we start with a guess known to be too small, and increase it by small steps. After each step, we check whether the new guess is close enough to the real answer; if not, we keep incrementing and checking.
# we are effectively checking all possible values g + k*increment for integer values of k, similar to guess and check
# in this algorithm we set two parameters: epsilon (the allowed difference between our approximation and the real answer), and the increment (the step size)
# the accuracy and performance of our algorithm depend heavily on these two values, in terms of both speed and accuracy
# decreasing the step size makes the algorithm run slower but get closer to the real answer, and vice versa with increasing epsilon (this speed/accuracy tradeoff shows up in similar forms elsewhere in numerical methods, e.g. Euler's method)

# e.g. example of the approximation algorithm
x = 36
epsilon = 0.0025
num_guess = 0
guess = 0.0
increment = 0.00000001

while abs(guess**2 - x) >= epsilon:
    guess += increment
    num_guess += 1
print(f"number of guesses {num_guess}")
print(f"{guess} is close to square root of {x}")
# number of guesses 599979170
# 5.999791671903779 is close to square root of 36

# to avoid overshooting our approximation, we can add an extra condition to the loop
x = 36
epsilon = 0.0025
num_guess = 0
guess = 0.0
increment = 0.00000001

while abs(guess**2 - x) >= epsilon and guess**2 <= x:
    guess += increment
    num_guess += 1
print(f"number of guesses {num_guess}")
if abs(guess**2 - x) >= epsilon:
    print(f"Failed on sqrt of {x}")
else:
    print(f"{guess} is close to square root of {x}")

# this shows that it's possible to overshoot past epsilon entirely, so sometimes other end conditions are better to include
# key takeaways from approximation: don't use == to check end conditions on floats; be careful that your looping mechanism can't skip over (jump past) the exit test; and there is always a tradeoff between efficiency and accuracy