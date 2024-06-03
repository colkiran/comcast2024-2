
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

x = int(input("Enter a number to find its fact :"))
print(f"The factorial of {x} is :{fact(x)}")

