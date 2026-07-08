## The practice problem for lecture 4 will be a binary password cracker. 
## Overview: this will combine all elements from class. You will get someone to assign you a number between 1 and 255 using an input function and write a guess and check loop that finds the secret number. 
# instead of guessing 1-255 using range with step size 1 use binary search. This means guess the midpoint, check if too high/low, and narrow the range.
# Use a found flag when the integer is found
# Then i want you to convert the secret number to binary using what was shown in the lecture

#e.g. code

secret_number= 124
low= 0 
high=255
guess= (low+high)//2
found = False

while low<= high:
    if guess==secret_number:
        found=True
        break
    elif guess<secret_number:
        low = guess +1
    else: 
         high = guess -1
    guess = (low + high)//2
if found:
    print(f"Found the secret number")
else:
    print(f"Secret number not found")

num = secret_number
result = ''
if num == 0:
     result = '0'
while num > 0:
     result = str(num%2) + result
     num = num//2
print(f"Secret number is {result}")

