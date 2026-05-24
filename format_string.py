name = "Andrey"
mide_name = "Andreevich"
balance = 123456

text = "hi {0} {1} you balance is {2}".format(name, mide_name, balance)
text_1 = "hi {name} {mide_name} you balance is {balance}".format(name=name, mide_name=mide_name)

print(text)
print(text_1)