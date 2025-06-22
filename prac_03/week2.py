"""def print_hash_lines():
    filename = input("Enter the filename: ").strip()
    file = open(filename, 'r')
    for line in file:
        if line.startswith("#"):
            print(line, end='')
    file.close()

print_hash_lines()"""

"""name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, file=out_file)
print("Done")"""

"""names = ["Lea", "Sam", "Bob"]

for name in names:
    filename = f"{name}.txt"
    with open(filename, "w") as file:
        file.write(name)"""

# Version 2

"""names = ["Bob", "Alice", "Charlie", "Monty"]

for index, name in enumerate(names, start=1):
    filename = f"{name}.txt"
    with open(filename, "w") as file:
        file.write(str(index))

names = ["Bob", "Alice", "Charlie", "Monty"]

for i in range(len(names)):
    name = names[i]
    filename = f"{name}.txt"
    with open(filename, "w") as file:
        file.write(str(i + 1)"""

"""with open("data.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

for i in range(0, len(lines), 2):
    name = lines[i].strip()
    country = lines[i + 1].strip()
    print(f"{name} was born in {country}")"""

# file = open("text2.txt")
# text = file.read()
# file.close
#
# print(text)

# with open("text2.txt") as file:
#     text = file.read()
#
# print(text)


result = int(input("Enter a valid integer: "))