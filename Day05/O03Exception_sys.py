import sys

n = int(input("Enter the numerator :"))
d = int(input("Enter the denaminator greater than zero (>0) :"))

print(f"Numerator   :{n}")
print(f"Denaminator :{d}")

try:
    q = n / d
    print(f"quotient :{q}")
except:
    print("Exception Occured.....")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
