
try:
    n = int(input("Enter the numerator :"))
    d = int(input("Enter the denaminator greater than zero (>0) :"))

    print(f"Numerator   :{n}")
    print(f"Denaminator :{d}")

    q = n / d

except ZeroDivisionError as z:
    print("Exception occured.....")
    print(z)
except ValueError as v:
    print("Exception occured.....")
    print(v)
except Exception as e:
    print("Exception occured.....")
    print(e)

else:
    print(f"Quotient is :{q}")
finally:
    print("Completed the division of numbers.....")