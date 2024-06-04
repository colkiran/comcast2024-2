
glbX = 100

def fun(x):                 # x is a local variable
    global glbX             # do not assign any value in this line
    print(f"x :{x}")
    glbX = 500
    print(f"glbx inside :{glbX}")


print(f'glbX before :{glbX}')

fun(25)

print(f"glbX after :{glbX}")
