def add(a, b, c):
    res = a + b + c
    return res

def addition(*nums):
    """
    Returns the sum of all the numbers passed as arguments
    Parameters:
    integers or floats or a mix of both
    return:
    integers or floats
    """
    total = sum(nums)
    return total

addition(8, 8, 8)

def build_profile(**kwargs): #dictionary key word args
    for k, w in kwargs.items():
        print(f'{k}: {w}')

def fancy_function(name, *nums, **kwargs):
    print(name)
    print(nums)
    print(kwargs)
# anonymous = lambda
#

square = lambda num: num * num

print(square(5))
res = square(2.9)
print(res)

surface_area_cylinder = lambda r, h: 22/7 * r**2 *2 + 22/7 *2 * r * h
print(surface_area_cylinder(5, 5))

people = [
    {'name': "Alex", 'age': 25},
    {'name': "Bob", 'age': 30},
    {'name': "Charlie", 'age': 40},
]
sort_by_age = sorted(people, key=lambda x: x['age'])
print(sort_by_age)

# build_profile(experience='100', name="Jane", age=20)



# call function
# print(add(9,7,5))

# print(addition(1,2,3))
# print(addition(1,2,3,4))
# print(addition(1,2,3,4,5))