
print("""Hello.Yes!""".split("."))


first_three = "abc"
result = "+".join(first_three)
print(result)

words = ["The","fox","jumped","over","the","fence","."]

one = "".join(words)
print(one)
one_string = " ".join(words)
print(one_string)

s = "    The        "
s = s.strip()
print(s)


equ = "All animals are equal."
equ = equ.replace("a", "@")
print(equ)

print("animals".index("m"))
print("animals".index("z"))

print("She said \"Surely.\"")
print("She said 'Surely'.")

fict = ["Tolstoy","Camus","Orwell","Huxley","Austin"]
print(fict[0:3])

ivan = """In place of death there was light."""
print(ivan[:17])
print(ivan[17:])
print(ivan[:])

