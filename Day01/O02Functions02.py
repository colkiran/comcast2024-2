
def test():
    from collections import namedtuple

    phy = 89
    che = 85
    mat = 92
    bio = 90
    eng = 80
    tml = 78

    nmdTpl = namedtuple("Marks", "p c m b e t")
    mrks = nmdTpl(p=phy, c=che, m=mat, b=bio, e=eng, t=tml)
    return mrks

marks = test()
print(marks)
print(f"Physics   :{marks.p}")
print(f"Maths     :{marks.m}")
print(f"Chemistry :{marks.c}")
print(f"Biology   :{marks.b}")
print(f"English   :{marks.e}")
print(f"Tamil     :{marks.t}")

