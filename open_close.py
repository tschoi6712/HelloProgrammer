
st = open("st.txt", "w")
st.write("Hello!")
st.close()

with open("st.txt", "w") as f:
    f.write('hi from Python!, happy coding!')


with open("st.txt", "r") as f:
    print(f.read())


my_list = list()
with open("st.txt", "r") as f:
    my_list.append(f.read())
print(my_list)


import csv
with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))



