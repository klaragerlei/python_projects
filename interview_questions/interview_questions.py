# REVERSE A STRING
s = 'hello world'

# Method 1: reverse for loop
reverse = ''
for i in reversed(s):
    reverse += i
print(reverse)

# Method 2: reverse join
reverse = ''.join(reversed(s))
print(reverse)

# Method 3: reverse indexing
reverse = s[::-1]
print(reverse)

###################################

# GET THE MOST COMMON CHARACTER IN A STRING
s = 'onomatopoeia'

# Method 1: dictionary
chars_dict = {}
for i in s:
    if i not in chars_dict:
        chars_dict[i] = 0
    chars_dict[i] += 1
print(max(chars_dict, key=chars_dict.get))

# Method 2: sorted list
sorted_chars = sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)
print(sorted_chars[0][0])

# Method 3: collections library
from collections import Counter
c = Counter(s)
print(c.most_common(1)[0][0])

###################################

# REMOVE DUPLICATES FROM A LIST
lst = ['dog', 'cat', 'dog', 'pig', 'cat']

# Method 1: for loop (always retains order)
unique = []
for item in lst:
    if item not in unique:
        unique.append(item)
print(unique)

# Method 2: set (doesn't always retain order)
unique = list(set(lst))
print(unique)

###################################

# GET THE SUM OF EVEN NUMBERS IN A LIST
nums = [1, 2, 3, 4, 5, 6]

# Method 1: for loop
total = 0
for num in nums:
    if num % 2 == 0:
        total += num
print(total)

# Method 2: list comprehension
total = sum([i for i in nums if i % 2 == 0])
print(total)

###################################

# FUND THE LONGEST WORD IN A STRING
s = 'This is a long string I promise'

# Method 1: for loop
longest_word = ''
longest_word_length = 0
for word in s.split(' '):
    if len(word) > longest_word_length:
        longest_word = word
        longest_word_length = len(word)
print(longest_word)

# Method 2: sorted list
sorted_words = sorted(s.split(' '), key=len, reverse=True)
print(sorted_words[0])
