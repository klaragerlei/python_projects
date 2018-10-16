def check_frequency(str, c):
    count = 0
    for i in str:
        if(i == c):
            count += 1
    return count


if __name__ == '__main__':
    str = input('Enter a string\n')
    c = input("Enter a character to check it's frequency\n")
    print(f'{c} appears {check_frequency(str, c)} times in the given string.')
