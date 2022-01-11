# Write a program that uses the filter function to print words which are palindromes in the word list passed.
# A palindrome is an expression that sounds the same when read from both the left and the right side.
# For example, such words are palindromes: radar, level, rotor.
word_list = ['level', 'madam', 'sister', 'kayak', 'book', 'rotator', 'runner', 'ice' ]

# Function
# def is_polindrome(word_list):
#     polindrome_list = []
#     for word in word_list:
#         if word == word[::-1]:
#             polindrome_list.append(word)
#     return polindrome_list
#
# print(is_polindrome(word_list))

# Lambda
polindrome_list = list(filter(lambda word: word == word[::-1], word_list))
print(polindrome_list)
