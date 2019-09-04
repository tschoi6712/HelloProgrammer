
my_tuple = tuple()
print(my_tuple)

rndm = ("M. Jackson", 1958, True)
print(rndm)

one = ("self_taught",)
print(one)

'''
dys = ("1984", "Brave New World", "Fahrenheit 451")
dys[1] = "Handmaid's Tale" #TypeError: 'tuple' object does not support item assignment
print(dys)
'''

dys = ("1984", "Brave New World", "Fahrenheit 451")
print(dys[2])
print("1984" in dys)
print("Handmaid's Tale" not in dys)



