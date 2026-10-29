from numbers import radius


def greet():
    print("Hello Hellen")

def greeting(name):
    print(f"Hello{name}")

def volume_cylinder(radius, height):
    v = 22/7 * radius**2 * height
    print(round(v))

def volume_cylinder2(radius, height):
    v = 22/7 * radius**2 * height
    return v

def volume_surface(radius, height):
    v = 22/7 * radius**2 * height
    a = 22/7 * radius**2 *2 + 22/7 * radius*2 *height
    return v, a


# greeting('Sila')
# greeting('Samia')
# greeting('Ahmed')
# volume_cylinder(radius=10, height=20)
# volume_cylinder(radius=8, height=18)


# greet() #call == use no arguments/ params == data

# result = volume_cylinder2(radius=5, height=5)
# print(result)
#
# with open("volumes.txt", "w") as file:
#     file.write(str(result))
volume, area = volume_surface(2, 2)
print(f"volume is {volume}, and area is {area}")

def divide(a, b, should_round):
    res= a/b
    if should_round == True:
        return round(res,2)
    else:
        return res


print(divide(9, 5.11,True))
# default parameters




