import json
from pathlib import Path

path = Path("user_dictionary.json")

user_dictionary = {}

print("Set an user data_dict now")

while True:
    print("What is you name?")
    username = input()

    print("Input you password?")
    password = input()

    print("If you end to set data press 'q'")
    q_input = input()

    user_dictionary["name"] = username
    user_dictionary["password"] = password

    if q_input == 'q':
        break

file = json.dumps(user_dictionary)
content = path.write_text(file)

print("Input you name: ")
input_name = input()

print("Input a password: ")
input_password = input()


#check json file is
save_data = json.loads(path.read_text())

usr_name = save_data['name']
usr_password = save_data['password']

if input_name == usr_name and input_password == usr_password :
    print("Welcome!!!")

else:
    print("Accesses denided!")

