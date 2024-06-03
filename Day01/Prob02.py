
def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

n = int(input("Enter the number of iteration :"))
for i in range(n):
    print(fibo(i), end=" ")

