print(f"Enter a two number and I divide first by second")

while True:
    
    print(f"Input first or 'q' to quite")
    first_num = input()

    if first_num == 'q':
        break


    print(f"Input second or 'q' to quite")
    
    second_num = input()

    if second_num == 'q':
        break

    try:
        answer = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print("Not divide by ZERO")
    else:
        print(f" Answer is {answer}")
    

