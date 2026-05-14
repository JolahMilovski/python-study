from pathlib import Path

path = Path("pi_di.txt")  # relative PATH





try:
    contents = path.read_text(encoding='utf-8').rstrip()

except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

#absolute Path
#path = Path("/home/Documents/code/python study/pi_di.txt")


print(f"formatting \n{contents}")

for line in contents.splitlines():   # thus method split file to line 
    print(f'\n New line is {line}')

with path.open('a') as f:
    f.write("\nAdd 777")


# Режимы открытия файлов для справки

#   Режим	Описание	Аналог в pathlib

#   'w'	Запись (перезапись)	write_text()
#   'a'	Дописывание (append)	open('a')
#   'x'	Эксклюзивное создание (ошибка если файл есть)	open('x')
#   'r'	Чтение	read_text()

contents  = "I love write code every day \n" 
contents += "I love write code every day \n"
contents += "I love write code every day \n"
contents += "I love write code every day \n"

with path.open('a') as f:
    f.write(contents)


#cont_of_words 

try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"File not found path {path}")

word = contents.split()
cont_of_words = len(word)

print(f'The file {path} has {cont_of_words} words')

contents_to_list = list(contents)
symbol = len(contents_to_list)

print(f"In this text {symbol} symbol")



