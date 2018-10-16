def count_vowels(str):
    vowelCount = 0
    for i in str:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vowelCount += 1
    return vowelCount


if __name__ == '__main__':
    str = input('Enter a string\n')
    print(f'Number of vowels are: {count_vowels(str)}')
