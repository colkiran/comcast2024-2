
def get_name(surname):
    print(f"surname is :{surname}")

    while True:
        name = yield
        print(f"Received :{name}")
        print("-" * 60)
        if surname in name:
            print(f"Surname found {surname} in {name}")

coObj = get_name("Pillai")
print(coObj)
coObj.__next__()
coObj.send("Sachin Tendulkar")
coObj.send("Yuvraj Singh")
coObj.send("Dhanraj Pillai")
