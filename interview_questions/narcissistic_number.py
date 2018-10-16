"""
A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original number. If this seems confusing, refer to the example below.

Ex: 153, where n = 3 (number of digits in 153)
13 + 53 + 33 = 153"""
import math
def is_narcissistic(i):
    actualsum=0
    size=math.ceil(math.log(i, 10)) #get length of number
    for n in range(size):
        actualsum += ((i//(10**n))%10)**size #multiply digits by size number
        if actualsum> i: #if the sum of digits > number then false finish for
            return False
    if actualsum == i: #if for ends, verify if sum is equal number
        return True
    else:
        return False
