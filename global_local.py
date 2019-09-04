x = 1
y = 2
z = 3
def f():
    print(x)
    print(y)
    print(z)
f()


def f():
    x = 1
    y = 2
    z = 3
    print(x)
    print(y)
    print(z)
f()


def f():
    x = 1
    y = 2
    z = 3
print(x)
print(y)
print(z)


x = 100
def f():
    global x
    x += 1
    print(x)
f()