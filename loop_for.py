# 100번(0~99) 반복문

for i in range(100):
    print("Hello, World!")

'''
for (i = 0; i < 100; i++) {
    console.log("Hello, World!");
}
'''

name = "Ted"
for character in name:
    print(character)


shows = ["GOT","Narcos","Vice"]
for show in shows:
    print(show)


coms = ("A. Development", "Friends", "Always Sunny")
for show in coms:
    print(show)


people = {"G. Bluth II":  "A. Development",
          "Barney": "HIMYM",
          "Dennis": "Always Sunny"
          }
for character in people:
    print(character)

'''
tv1 = ["GOT", "Narcos", "Vice"]
i = 0
for i in tv1:
    new = tv1[i].upper() # TypeError: list indices must be integers or slices, not str
    tv1[i] = new
    i += 1
print(tv1)
'''


tv2 = ["GOT", "Narcos",  "Vice"]
for i, name in enumerate(tv2):
    new = tv2[i]
    new = new.upper()
    tv2[i] = new
print(tv2)


tv3 = ["GOT", "Narcos", "Vice"]
coms3 = ["Arrested Development",  "friends", "Always Sunny"]
all_shows = []
for show in tv3:
    show = show.upper()
    all_shows.append(show)
for show in coms3:
    show = show.upper()
    all_shows.append(show)
print(all_shows)


for i in range(0, 100):
    print(i)
    break

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


for i in range(1, 3):
    print(i)
    for letter in ["a", "b", "c"]:
        print(letter)


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)
