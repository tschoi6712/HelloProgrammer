
my_dict1 = dict()
print(my_dict1)

my_dict2 = {}
print(my_dict2)

fruits = {"Apple": "Red",
          "Banana": "Yellow"
          }
print(fruits)

facts = dict()
# add a value
facts["code"] = "fun"
facts["Bill"] = "Gates"
facts["founded"] = 1776
# lookup a key
print(facts["founded"])
print(facts)

bill = dict({"Bill Gates": "charitable"
             })
print("Bill Gates" in bill)
print("Bill Gates" not in bill)

books = {"Dracula": "Stoker",
         "1984": "Orwell",
         "The Trial": "Kafka"}
del books["The Trial"]
print(books)

