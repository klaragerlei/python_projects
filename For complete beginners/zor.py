def myXOR(x, y):
	return ((x | y) & (~x | ~y))     #used bitwise and(&) and or(|)

n = int(input("Enter first number  :"))
n1 = int(input("Enter 2nd number  :"))
print("XOR of " ,n," and ",n1," is ", myXOR(n, n1))