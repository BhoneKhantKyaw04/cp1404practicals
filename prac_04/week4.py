"""names = ["Ada", "Alan", "Bill", "John"]
name_to_remove = "start"

while name_to_remove != "":
    print(", ".join(names))
    name_to_remove = input("Who do you want to remove? (Press enter to stop) ")

    if name_to_remove == "":
        break

    if name_to_remove in names:
        names.remove(name_to_remove)
        print(f"{name_to_remove} removed.")
    else:
        print(f"{name_to_remove} is not in the list.")

print("Final list:", ", ".join(names))"""

"""def get_numbers():
    user_input = input("Enter numbers: ")
    try:
        numbers = [float(num.strip()) for num in user_input.split(",") if num.strip() != ""]
        return numbers
    except ValueError:
        print("Please enter only valid numbers")
        return []

def square_numbers(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2

def display_numbers(numbers):
    for num in numbers:
        print(num, end=". ")

def main():
    numbers = get_numbers()
    square_numbers(numbers)
    numbers.sort()
    display_numbers(numbers)
               
main()"""

def display_scores(data):
    for item in data:
        if isinstance(item, list):
            print(f"{item[0]}")
            print(f"= {item[1]}")
        elif isinstance(item, str):
            name = item
        elif isinstance(item, (int, float)):
            print(f"{name}")
            print(f"= {item}")

data = ['Derek', 71, ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
display_scores(data)

