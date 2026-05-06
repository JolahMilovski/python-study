list_of_abrakadabra =['qwerqwerqwer','asdfasdfasdfasdf','werrfvrfvrfv','tgbtgbtgb','yhnyhnyhn','ujmujmujm']

def print_abra(list_of_word):
    for word in list_of_word:
        print(word)

print_abra(list_of_abrakadabra)






def greate_user(username):
    '''предупреждает о начале хеллоуина'''
    print(f"Hellowing START, afrade a {username}!!!!")

username = "Kenny"
greate_user(username)


def all_my_friend(first_name, last_name, age=25):
    print(f'First name is {first_name.title()}')
    print(f'Last name is {last_name.title()}')
    print(f'His age is {age}')
    full_info = f"{first_name} {last_name} {age}"
    return full_info.upper()
    

return_function_value = all_my_friend("asd", 'asqwe', 12)
print(return_function_value)
return_function_value = all_my_friend("dfgd", 'rtgqwe', 15)
print(return_function_value)
return_function_value = all_my_friend("dfgd", 'rtgqwe')
print(return_function_value)

def all_my_friend_dict(first_name, last_name, age=25):
    print(f'First name is {first_name.title()}')
    print(f'Last name is {last_name.title()}')
    print(f'His age is {age}')
    
    # Возвращаем словарь
    friend_dict = {
        'first_name': first_name.title(),
        'last_name': last_name.title(),
        'age': age,
        'full_name': f"{first_name.title()} {last_name.title()}"
    }
    return friend_dict

# Использование
return_function_value = all_my_friend_dict("asd", 'asqwe', 12)
print(return_function_value)

return_function_value = all_my_friend_dict("dfgd", 'rtgqwe', 15)
print(return_function_value)

return_function_value = all_my_friend_dict("dfgd", 'rtgqwe')
print(return_function_value)

"""add name & title to dict"""
def make_album(artist_name, album_title):
    album_info ={"artist_name": artist_name, "album_title":album_title}
    return album_info 

"""add song's count to dict"""
def add_count_of_song(album_info, count_of_song=12):
    print(f'Input count of song')

    count = input()
    if count.isdigit() == '':
        count = count_of_song

    album_info['count_of_song'] = count
    return album_info 


muz_album_param = True

write_your_album =[]

while muz_album_param:
    print("Input artist name: ")
    artistname = input()

    print("Input album title: ")
    albumtitle = input()

    album = make_album(artistname, albumtitle)

    add_count_of_song(album)

    write_your_album.append(album)
    print("Your are remember any album? y/n")
    resault = input()

    if resault == 'q':
        break  

print("\n" + "="*40)

print(write_your_album)