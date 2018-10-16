def check_palindrome(str):
    reversedStr = ''.join(reversed(str))
    if str.casefold() == reversedStr.casefold():
        print(f'{str} is a palindrome')
    else:
        print(f'{str} is not a palindrome')


if __name__ == '__main__':
    str = input('Enter a string\n')
    check_palindrome(str)
