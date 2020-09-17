driving = input('Have you driving before?')
if driving != 'Yes' and driving != 'No':
    print('Your have to enter Yes/No')
    raise SystemExit

age = input('Please enter you age? ')
age = int(age)
if driving == 'Yes':
    if age >= 18:
        print('You have passed the test')
    else:
        print('That is strange')
elif driving == 'No':
    if age >= 18:
        print('You can take driving test now')
    else:
        print('Good, you can take driving test in near furture!')
