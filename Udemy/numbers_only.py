# User will type something, though a number is required
# If they type a number, an answer will appear. If not, the system will show an error

number = input('Type a number: ')

if number.isnumeric():
    number = pow(float(number),2)
    print(f'The answer is: {number}')
else:
    print('Error! This is not a number')
