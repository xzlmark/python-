number = 23
running = True

while running:
    guess = int(input('enter an integer:'))
    if guess == number:
        print('guess ok')
        running = False
    elif guess < number:
        print('NO,it is little')
    else:
        print("it too lagee")
else:
    print('循环结束')
print('Done')