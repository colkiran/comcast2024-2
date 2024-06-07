
l1  = [x ** 2 for x in range(1, 11)]        # comprehension
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = (x ** 2 for x in range(1, 11))     # generator
print(f"l2 :{l2}")
print(type(l2))

print(l2.__next__())
print(l2.__next__())
print(l2.__next__())
print(l2.__next__())
print(l2.__next__())

print("-" * 60)
s1 = sum([x ** 2 for x in range(1, 11)])
print(f"sum of squares using comprehension :{s1}")

s2 = sum((x ** 2 for x in range(1, 11)))
print(f"sum of squares using generators :{s2}")

print("-" * 60)
from sys import getsizeof

t1 = [x ** 2 for x in range(1, 10000)]
print(f"Comprehension size of the list :{getsizeof(t1)}")

print("-" * 60)
t2 = (x ** 2 for x in range(1, 10000))
print(f"Generator size of the list :{getsizeof(t2)}")


