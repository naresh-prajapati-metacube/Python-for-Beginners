class InvalidPasswordException(Exception):
    """Raised when the input value is too large"""
    pass


password = input('Please enter your password: ')

try:
    if(len(password) > 8):
        raise InvalidPasswordException
    else:
        print('Valid password')
except InvalidPasswordException:
    print('Password can not be large than 8 characters')
except:
    print('Something went wrong!!')