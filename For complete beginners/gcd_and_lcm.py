n1 = int(input("Enter first number :"))
n2 = int(input("Enter second number :"))

def gcd(n1, n2):
	if n1 == n2:
		return n1
	if n1 > n2:``
		return gcd(n1-n2, n2)
	return gcd(n1, n2-n1)

GCD = gcd(n1, n2)
print("Gcd of ",n1, "and", n2, "is", GCD)

lcm = (n1 * n2)/ GCD
print("lcm of ",n1, "and", n2, "is", lcm)