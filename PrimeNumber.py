number = int(input('Please Enter a number: '))

isPrimeNumber = True

checkNumber = (number - 1)

while checkNumber > 1:
    if(number%checkNumber == 0):
        isPrimeNumber = False
    checkNumber=(checkNumber-1)

if(isPrimeNumber):
    print('Prime No')
else:
    print('Not a Prime No')