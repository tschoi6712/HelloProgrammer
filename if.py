'''
If (expression) Then
           (code_area1)
Else
           (code_area2)
'''
home = "America"
if home == "America":
    print("Hello, America!")
else:
    print("Hello, World!")

home = "Canada"
if home == "America":
    print("Hello, America!")
else:
    print("Hello, World!")

home = "America"
if home == "America":
    print("Hello, America!")

# 홀수 짝수 판별
x = 2
if x == 2:
    print("The number is 2.")
if x % 2 == 0:
    print("The number is even.")
if x % 2 != 0:
    print("The number is odd.")

x = 10
y = 11
if x == 10:
    if y == 11:
        print(x + y)

home = "Thailand"
if home == "Japan":
    print("Hello, Japan!")
elif home == "Thailand":
    print("Hello, Thailand!")
elif home == "India":
    print("Hello, India!")
elif home == "China":
    print("Hello, China!")
else:
    print("Hello, World!")
