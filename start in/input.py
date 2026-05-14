message = input("Please input some dollars and say: ")
print(message)

name = input(f'Please, input you name: ')
print(f'Hello {name}')

# for writing a several line input

prompt = "If you share your name, we can personalize the message you see"
prompt += "\n What is you first name?\n"

name = input(f'\t Hello {prompt}')

print(name)

#st34mp4ss = "fRdkB12(34Dyrg@hi^gkb)"

prompt = "This video is 19+"
prompt += "\n How old are you? \n"

age = int(input(prompt))
if age > 19:
    print("You are welcome")
