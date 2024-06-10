import time
from collections import namedtuple

DATA_SET_A = {
    'Foo': "Bar",
    "Baz": [5, 7, 11],
    "Qux": {"A": "Boston", "B": "Python", "C": "TDD"}
}

DATA_SET_B  = DATA_SET_A        # shallow copy

DATA_SET_C = {
    "Foo": "Bar",
    "Baz": [3, 5, 7],
    "Qux": {"A": "Boston", "B": "Python", "C":"TDD"}
}



