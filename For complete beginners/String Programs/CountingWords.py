def count_words(str):
    return len(str.split())


if __name__ == '__main__':
    str = input('Enter a string\n')
    print(f'Number of words: {count_words(str)}')
