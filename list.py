
fruit = list()
print(fruit)

fruit = []
print(fruit)

fruit = ["Apple", "Orange", "Pear"]

print(fruit)
fruit.append("Banana")
print(fruit)
fruit[3] = "Peach"
print(fruit)

print(fruit[0])
print(fruit[2])
print(fruit[5])  # IndexError: list index out of range


colors = ["blue","green","yellow"]
print(colors)
item = colors.pop()
print(item)
print(colors)

boolean1 = "green" in colors
boolean2 = "black" not in colors
print(boolean1)
print(boolean2)
print(len(colors))

colors1 = ["blue", "green", "yellow"]
colors2 = ["orange", "pink", "black"]
print(colors1 + colors2)