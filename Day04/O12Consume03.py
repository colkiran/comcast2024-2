
import sys

sys.path.append("C:/Delhi")
print([path for path in sys.path])

import gurgaon.mymodule as m
from gurgaon.mymodule import Employee

print(m.gstname)
print("-" * 60)

emp1 = Employee("Richard", 90000)
print(emp1)
