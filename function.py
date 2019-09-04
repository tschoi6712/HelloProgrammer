'''
def [function_name]([parameters]):
    [function_definition]

def add(x, y):
    """
    Returns x + y.
    :param x: int.
    :param y: int.
    :return: int sum of x and y.
    """
    return x + y
'''

def f(x):
    return x * 2

def f():
    return 1 + 1
result = f()
print(result)

def f(x, y, z):
    return x + y + z
result = f(1, 2, 3)
print(result)

def f():
    z = 1 + 1
result = f()
print(result)

def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")
print(even_odd(2))
print(even_odd(3))

def add_it(x, y=10):
    return x + y
result = add_it(2)
print(result)

def f(x=2):
   return x**x
print(f())
print(f(4))


