def compose2(f, g):
    return lambda x: f(g(x))                    #lambda function helps to define a one line function

def compose3(f, g):
    return lambda x: g(f(x))

def double(x):
    return x * 2

def incmnt(x):
    return x + 1

num=int(input("Enter the number   :"))

i = compose2(double, incmnt)

print("This answer is by first calling icmnt and then double function  :",i(num))           #passing function as argument
j = compose3(double,incmnt)
print("This answer is by first calling double and then icmnt function  :",j(num))