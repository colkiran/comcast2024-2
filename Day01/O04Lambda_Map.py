"""
def sqr(x):
   return x ** 2
l = (1, 2, 3, 4, 5)

res = map(sqr, l)

"""

l = list(range(1, 11))
print(f"l :{l}")

res = list(map(lambda x: x ** 2, l))

print(f"res :{res}")

print("-" * 60)
# sort these months using a map function
# ----------------------------------------
months = ['dec', 'oct', 'jul', 'nov', 'aug', 'sep', 'mar', 'jan', 'apr', 'jun', 'feb', 'may']

print(f"unsorted Months :{months}")
# sort or sorted
from calendar import  month_abbr
print(f"month_abbr :{list(month_abbr)}")

res = sorted(months, key = list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print("-" * 60)
print(f"Sorted Months :{res}")