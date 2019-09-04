# 예외처리

a = input("type a number: ")
b = input("type another number: ")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")


try:
    a = input("type a number: ")
    b = input("type another: ")
    a = int(a)
    b = int(b)
    print(a / b)
except(ZeroDivisionError, ValueError):
    print("Invalid input.")

'''
#NameError: name 'c' is not defined
try:
    10 / 0
    c = "I will never get defined."
except ZeroDivisionError:
    print(c)    
'''

try:
    "animals".index("z")
except:
    print("Not found.")
