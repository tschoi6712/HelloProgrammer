
colors = ["purple", "orange", "green"]
guess = input("Guess a color:")

if guess in colors:
    print("You guessed correctly!")
else:
    print("Wrong! Try again.")


lists = []
rap = ["Kanye West", "Jay Z", "Eminem", "Nas"]
rock = ["Bob Dylan", "The Beatles", "Led Zeppelin"]
djs = ["Zeds Dead", "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)

rap = lists[0]
print(rap)

rap.append("Kendrick Lamar")
print(rap)
print(lists)

eights = ["Edgar Allan Poe", "Charles Dickens"]
nines = ["Hemingway", "Fitzgerald", "Orwell"]
authors = (eights, nines)
print(authors)