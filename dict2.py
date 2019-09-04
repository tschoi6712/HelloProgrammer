
rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
          }
n = input("Type a number: ")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")


bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"
        }
my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)


ny = {"location":
      (40.7128,74.0059),

      "celebs":
      ["W. Allen", "Jay Z", "K. Bacon"],

      "facts":
      {"state": "NY",  "country": "America"}
}
print(ny)