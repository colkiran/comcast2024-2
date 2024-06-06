
import sys

for path in sys.path:
    print(path)

import gurgaon.mymodule as m
from gurgaon.mymodule import Employee

print(m.gstname)
print("-" * 60)

emp1 = Employee("Louis", 90000)
print(emp1)
