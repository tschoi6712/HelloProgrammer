upper = "Hello".upper()
print(upper)

cap = "four score and...".capitalize()
print(cap)

replace = "Hello".replace("o", "@")
print(replace)

author = "Kafka"
print(author[0])
print(author[-1])
#print(author[5])  #IndexError: string index out of range
print(author[-3])

print("cat " + " in" + " the" + " hat")
print("Sawyer  " * 3)

print("William {}".format("Faulkner"))

last = "Faulkner"
print("William {}".format(last))


author = "William Faulkner"
year_born = "1897"
print("""{} was born in {}.""".format(author, year_born))


n1 = input("Enter a noun: ")
v = input("Enter a verb: ")
adj = input("Enter an adj: ")
n2 = input("Enter a noun: ")
r = """The {} {} the {} {}
    """.format(n1, v, adj, n2)
print(r)