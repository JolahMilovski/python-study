from name_function import get_formatted_name

print(" Enter 'q' to quite ")

while True:
    first = input("\n Please input a a first name: ")
    if first == 'q':
        break
    last = input("INput last name: ")
    if last == 'q':
        break

    middle = input("Input middle name: ")
    if middle == 'q':
        break

    format_name = get_formatted_name(first, middle,last)
    print(f"Formatted name: {format_name}")

