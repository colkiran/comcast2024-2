
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.....")


def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.....")


# city is a default argument and gname is a non default argument
def greetGstCty(gname,  city = "Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.....")


greet()

print("-" * 60)

greetGst("Sachin")
greetGst("Rahul")

print("-" * 60)

greetGstCty("Sunil Gavaskar")
greetGstCty("Rohit Sharma")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)
# named Args
def admisn(fnm, lnm, dob, gender, qlf, city, cno, mailid, address, adhrno):
    print(f"Name          :{fnm} {lnm}")
    print(f"DOB           :{dob}")
    print(f"Gender        :{gender}")
    print(f"Qualification :{qlf}")
    print(f"City          :{city}")
    print(f"Contact No.   :{cno}")
    print(f"Email ID      :{mailid}")
    print(f"Address       :{address}")
    print(f"Adhar         :{adhrno}")

admisn(city="Chennai", adhrno="239420", dob="18/03/1993", fnm="Kevin", lnm="Costner", mailid="kevin@gmail.com", address="Anna Nagar, 8th Cross", gender="Male", cno="902300482", qlf="Mtec")

print("-" * 60)
# variable length arguments - *args, **kwargs
# *numbers - can accept more than one argument - stores it in a tuple
def productAll(*numbers):
    print(numbers)
    print(*numbers)     # unpacking
    prod = 1
    for number in numbers:
        prod *= number

    return prod

res = productAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)

def extract_details(**detail):
    print(detail)
    for k, v in detail.items():
        print(k, "=>", v)

extract_details(name="Dhoni", age=32, runs=75, oppn= "Aus", venue="Chepauk")

print("-" * 60)
def multiplyMe(x, y):
    return x * y

print("%i x %i = %i" % (10, 20, multiplyMe(10, 20)))

# Recursive Calls - functions calling itself
# factorial of a number, Fibanoccci series

print("-" * 60)
def arithCalc(x, y):
    add = x + y
    diff = x - y
    prod = x * y
    quot = x / y

    return add, diff, prod, quot

res = arithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)

def fun():
    # this is a comment
    "this is a doc string"
    print("hello world")

fun()
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    1. if both x and y are integers then the result would be the sum of numbers
    2. if x and y are strings then the result will be a concatenated string
    3. if x and y are variables of two different data types then the result will be and error
    """
    print("Hello World")
    return x + y

print(fun1(10, 20))
print(fun1("good", "blood"))

print("=" * 60)
help(fun1)







