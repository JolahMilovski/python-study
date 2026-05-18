user_input = input("Input (разделяйте пробелами): \n")

symbol_string = ""
integers = []
floats = []

# Разбиваем на токены по пробелам
tokens = user_input.split()

for token in tokens:
    if '.' in token and token.replace('.', '').isdigit():
        # Это float
        floats.append(float(token))
    elif token.isdigit():
        # Это целое число
        integers.append(int(token))
    else:
        # Это строка
        symbol_string += token + " "

print(f"Строка: '{symbol_string.strip()}'")
print(f"Целые: {integers}")
print(f"Float: {floats}")

a = int(input())
print(a)