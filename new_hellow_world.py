message = "Hellow world "
print(message)
message22 = "Hellow world 22"
print(message.title())
print(message.upper())
print(message22.lower())

two_message = f"{message}{message22}"
print(two_message)

new_strip_variable = ' variable with a strip '
print(new_strip_variable)
print(new_strip_variable.rstrip())
print(new_strip_variable.strip())

new_url = "https://ya.ru"
print(new_url)

new_url_without_prefix=new_url.removeprefix('https://')
print(new_url_without_prefix)

message = 'One of Python\'s strengths is its diverse community.'
print(message)

'''multiply assigment'''
x,y,z='qwe', 'wer', 'ert'
xyz=f'{x}{y}{z}'

print(xyz)

#CONSTANT

FIRST_CONSTANT=1000
print(FIRST_CONSTANT)



