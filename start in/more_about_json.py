from pathlib import Path
import json

number = [1,2,3,4,5,6,7,12,23,34,45,56,67,45,34,23]

Path('my_json.json').write_text(json.dumps(number))

path = Path('my_json.json')

contents = path.read_text()

list_of_number = (json.loads(contents))

list_of_number.append(22)

print(list_of_number)


