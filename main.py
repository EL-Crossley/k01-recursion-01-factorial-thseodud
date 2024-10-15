3# Put your function here
def factorial(n):
        x = int(n)
        if (x < 1 ):
                return "Invalid number"
        if x == 1:
                return n
        elif (x > 1):
                return x *factorial(x-1)
        

# testing
num = int(input(""))
print(factorial(num))