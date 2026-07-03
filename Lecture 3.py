# Lecture 3: Iteration, Loops
# The main topics covered will be program flow and loops


# Control Flow: WHILE LOOPS

# Syntax:
# while <condition>:
#     <code>
#     <code>

# <condition> evaluates to a Boolean.
# If it returns True, then it executes all the steps inside the while code block.
# The condition is checked every time, and the code block will repeat until <condition> is False.
# If <condition> is never False, then it will loop forever.


# Example: countdown launch utilizing while loop
# Run code in IDE

# countdown = 5
# while countdown > 0:
#     print(f"Launching in {countdown}...")
#     countdown -= 1
#
# print("Blast off!")


# while loops can repeat code inside indefinitely,
# and sometimes they require manual intervention to end the program.


# Example: Birthday celebration message using while loop
# Run code in IDE

# print("Write your DOB in the following format: MM/DD/YYYY")
# birthday = input("When were you born?: ")
#
# candles = 5
#
# print("\nBirthday celebration starting!")
#
# while candles > 0:
#     print(f"Blowing out candle {candles}...")
#     candles -= 1
#
# print("All candles are out!")
# print("Happy Birthday!")
# print(f"Your birthday is saved as: {birthday}")


# Iterating Through Numbers With While Loops

# To iterate through numbers in a sequence, you must set the loop variable outside the while loop
# and test the loop variable in the condition/while loop.
# You must increment the loop variable inside the while loop,
# and it must change in some way or else the condition will always be true.


# A common pattern to know about is the factorial loop.
# i is our loop variable, and for our while loop we are doing a conditional check
# and incrementing the loop variable inside the while loop.


# Example: factorial loop
# Run code in IDE

# x = 5
# i = 1
# factorial = 1
#
# while i <= x:
#     factorial *= i
#     i += 1
#
# print(f"{x} factorial is {factorial}")


# i += 1 is equivalent to i = i + 1
# factorial *= 2 is equivalent to factorial = factorial * 2


# FOR LOOPS

# for loops allow us to rewrite loops in a more efficient way.
# Iterating through numbers in a sequence can be cut short in comparison to a while loop.
# If there is a sequence of values you ever want to iterate over,
# that is what for loops are useful for.


# Example:
# Run code in IDE

# for n in range(5):
#     print(n)


# Syntax for a for loop looks as follows:

# for <variable> in <sequence of values>:
#     <code>

# Each time through the loop, <variable> takes a value.
# First time, <variable> takes the first value,
# and next time it takes the second value,
# and so on until it runs out of values.


# A common sequence is much like the example above:

# for <variable> in range(<some_num>):
#     <code>
#     <code>

# The variable starts at 0 and keeps going to the next variable
# until it gets to some_num - 1.
# for loops only repeat for however long the sequence is.
# The loop variable takes on these values in order.


# RANGE

# range generates a sequence of integers, following a certain pattern.

# range(start, stop, step) is the format where:
# start is the first int generated,
# stop controls the last int generated, up to but not including this int,
# and step is used to generate the next int in the sequence.

# The process for range is very similar to slicing in strings.


# Example:
# Run code in IDE

# for i in range(4):
#     print(i)

# The start defaults to 0 and the step defaults to 1.


# RUNNING SUM

# mysum is a variable used to store the running sum.
# It works like memory storage.
# When combined with range, it adds the ints sequentially.


# Example:
# Run code in IDE

# mysum = 0
#
# for i in range(10):
#     mysum += i
#
# print(mysum)