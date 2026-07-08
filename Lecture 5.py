## LECTURE 5: Looking at floats in binary and working on more basic algorithms

## FRACTIONS IN BINARY
# for binary representation we use the idea a*2**-1 + b*2**-2 + c*2-3 and so on
# so this means that the binary representation of a decimal fraction f would require finding the values of a, b, c, etc so f= 0.5a + 0.25b + 0.125c + 0.0625 d and so on
# to find this representation the idea is that if we can find a power of 2 big enough to turn it into a whole number, can convert to binarym and then divide by the same power of 2 to restore it
# if there is no integer p such that x*(2**p) is a whole number then the internal representation is always an approxiamtion, but i am assuming that the representation for the decimal fraction is completely accurate and not an approximation
# so floating point conversion works preciselyt in some cases but not in others as some may have a power opf 2 that converts to a whole number and the other doesnt

# e.g.

x= 0.625
p=0
while ((2**p)*x)%1 !=0: # grabs decimal part
    print("remainder= " + str((2**p)*x - int((2**p)*x )))
    p+=1
#this portion finds the woer of 2 to make integer 
num = int((2**p)*x ) #converts to integer 

result = ''
if num == 0:
     result = '0'
while num > 0:
     result = str(num%2) + result
     num = num//2
# getting binary number 
for i in range(p-len(result)):
     result = "0" +result
#pad front with appropriate number of zeros 

result= result[0: -p] + "." + result [-p:] #add decimal point 
print(f"The binary representation of the decimal {str(x)} is {str(result)}")

# through this we can see that this is a very long and tedious process but ultimatley everything is reporesented in terms of bits 
# real numbers are a bit harder to represent and typically pose some problems because sometimes we have to somehow approximate the potentially infinite binary sequence of bits needed to represent these real numbers 

## Storing floating point numbers #.#
# a floating point is a pair of integers so there is a significant digit and a base 2 exponent 

# e.g. (1,1) here the first 1 is our significant digit and the second 1 is out base 2
# (1,1) is equal to 1*2**1
# 1*2**1 is equal to 10base2 
# = 2.0

# we do this because we want to know the error in our programs and why it happens. It happens because computers only have a certain amount of space to store data
# most modern computers only have 32-64 bits of storage to represent significant digits
# if a number is represented with more than 32-64 bits in binary the computer cannot store this information and so the number will be rounded 
# because of errors like these we never want to use == to test floats, we want to test whether or not they are within a small range (epsilon) of each other 
# because of these errors as well we need to be careful when desigining anything in python using floats

# a way to use this knowledge and implement it into our guess and check algorithm to make it more accurate is by using something called the approximation algorithm 
# this is better than guess and check because it allows us to find an approximation to an answer and not just whether or not it was found or not
# the approximation algorithm is not there to give an exact answer but an answer that is "close enough" or an approxiamtion hence its name

## APPROXIMATION

#for approximation we want to find an answer that is good enough (within a certain distance to the real answer)
# to do this we must start with a guess known to be too small and incrememnt it by small values. Check the new value to see if it is close enough to the real answer, and if not continue the process of incrementing and testing. 
# we are looking at all possible values g+k*a for integer values of k, similar to guess and check 
# in this algorithm we must set two parameters: the epsilon (the difference between approximationand real answer), and the increment (essentially step size)
# the accuracy and performane of our algorithm will vary based on these values in both speed and accuracy 
# decreasing the step size will make the algorithm run slower but will ultimately get closer to the real answer and vice versa with increasing epsilon(very similar to Euler's formula)

#e.g. example of approximation algorithm 
x= 36 
epsilon = 0.0025
num_guess = 0
guess = 0.0 
increment = 0.00000001

while abs (guess**2 - x) >= epsilon:
     guess+= increment
     num_guess +=1 
print (f"number of guesses {num_guess}")
print (f"{guess} is close to square root of {x}")
#number of guesses 599979170
#5.999791671903779 is close to square root of 36