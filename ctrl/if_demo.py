
number = 59
guess = int(input('enter an integer:'))
print('guess is:'+ str(guess))
while 1:
    if guess>number:
        print('差大了')
        guess = int(input('enter an integer:'))
        print('guess is:' + str(guess))
    elif guess<number:
        print('差小了')
        guess = int(input('enter an integer:'))
        print('guess is:' + str(guess))
    else:
        print('差中了')
        break

print('done')
