
def fun(plr):
    print(f"plr :{plr}")
    plr.append("kholi")
    plr.append('dhoni')
    print(f"plr inside :{plr}")


plyrs = ['sachin', 'sourav', 'sehwag', 'yuvraj']
print(f"plyrs before  :{plyrs}")

fun(plyrs)

print(f"plyrs after  :{plyrs}")
