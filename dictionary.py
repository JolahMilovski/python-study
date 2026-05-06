alien_0 = {"color" : "green", 'point': 5}
print(alien_0["color"])
print(alien_0["point"])
alien_0['health'] = 40 
print(alien_0)
alien_0['def'] = 4000
print(alien_0)
alien_0["x_position"] = 0

alien_0["speed"] = ["slow"]
if alien_0["speed"] == 'slow':
    alien_0["x_position"] += 1

elif alien_0["speed"] == "medium":
    alien_0["x_position"] += 2

elif alien_0["speed"] == "fast":
    alien_0["x_position"] += 3


del alien_0["def"]

print(alien_0)

#Таблица методов
#Метод	Описание
#get(key[, default])	Возвращает значение по ключу или default
#setdefault(key[, default])	Возвращает значение или устанавливает и возвращает default
#update([other])	Обновляет словарь парами из другого словаря
#pop(key[, default])	Удаляет ключ и возвращает значение
#popitem()	Удаляет и возвращает последнюю пару
#clear()	Очищает словарь
#keys()	Возвращает view всех ключей
#values()	Возвращает view всех значений
#items()	Возвращает view всех пар (ключ, значение)
#copy()	Создаёт поверхностную копию
#fromkeys(seq[, value])	Создаёт словарь из последовательности ключей


user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}


for key, value in user_0.items():
    print(f'\n Key: {key}')
    print(f'\n Value: {value}')


favorite_lang ={
    "jen":"pu",
    "ter":"erf",
    "xcv":"tgb",
    "qwer":"erty"
}
# метод item для обращения ко всем параметрам словаря
for n, l in favorite_lang.items():
    print(f'{n.title()} is a fav lang of {l.title()}')

# метод key() для обращения к ключу словаря 

for name in favorite_lang.keys():
    print(name.title())

for n in favorite_lang.values():
    print(n.title())

# dictionary in list

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
print(aliens)


#dic in dic

users = {
    'aeinstein': 
        {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': 
        {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")







