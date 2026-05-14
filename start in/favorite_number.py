import json
from pathlib import Path

path = Path("my_favorite_number.json")

def store_favorite_nunber():
    
    print("Inter is you favorite number?")

    favorite_number = input()

    path.write_text(json.dumps(favorite_number))

def read_favorite_nummber():

    print("Your favorite number is: \n")

    content_from_file = path.read_text()

    content = (json.loads(content_from_file))

    print(content)

def check_favorite_number():

    file_content = path.read_text()

    load_conternt = (json.loads(file_content))

    if load_conternt == "":
        print('my_favorite_number.json is empty')        






try:
    read_favorite_nummber()

except json.JSONDecodeError:
    
    print("Файл пуст")
    store_favorite_nunber()

read_favorite_nummber()




