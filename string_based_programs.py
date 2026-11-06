"""
    ## 1. check string palindrome or not.
"""

def check_palindrome(st):
  st1= st[::-1]
  if st == st1:
    return "palindrome.!"
  return "not palindrome.!"
print(check_palindrome("madam"))
print(check_palindrome("sir"))

# output:
# palindrome.!    
# not palindrome.!

"""
    ## 2. count vowels in a string.

"""

def count_vowels(s):

  return len([ i for i in s if i in 'aeiou'])

s = "python programming"
print(count_vowels(s))
print(count_vowels('vaaisuu'))

# output:
# 4
# 5

"""
## 3. Find the uppercase and lowercase characters in a string.

"""
def find_lowercase_and_uppercase(s):
  lower = 0
  upper = 0
  for i in s:
    if i.islower():
      lower += 1
    elif i.isupper():
      upper += 1

  return f'lower : {lower} and upper : {upper}'

print(find_lowercase_and_uppercase("Python Programming"))

"""

## 4. find the duplicte characters in a string.

"""

def find_duplicate_characters(s):

      return '-'.join(set(i for i in s if s.count(i)>1))

print(find_duplicate_characters("python programming"))

# output:
# m-g-r-p-n-o

"""
## 5. Find the first non-repeating character

"""

def find_first_non_repeating_char(s):
    
    for i in s:
      if s.count(i) == 1:
          print(i)
          break
find_first_non_repeating_char("swiss")

# output:
# w

"""
## 6.Find the first repeating character

"""

def find_first_repeating_char(s):
    
    for i in s:
      if s.count(i) > 1:
          print(i)
          break
find_first_repeating_char("python programming")

"""
## 7. Count the frequency of each character

"""

def frequency_count_of_each_char(s):
    return {ch: s.count(ch) for ch in s}

print(frequency_count_of_each_char("programming"))
print(frequency_count_of_each_char("developer"))

# output:
# {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
# {'d': 1, 'e': 3, 'v': 1, 'l': 1, 'o': 1, 'p': 1, 'r': 1}

"""
## 8. Reverse a string without using any inbuilt method.

"""

def reverse_the_string_without_inbuilt(s):
      return ''.join([s[i] for i in range(len(s)-1,-1,-1)])

print(reverse_the_string_without_inbuilt('vasu'))
print(reverse_the_string_without_inbuilt('python'))
print(reverse_the_string_without_inbuilt('hello'))

# output:
# usav
# nohtyp
# olleh

"""
## 9. Check whether two strings are anagrams?

"""

def check_anagram(s1,s2):
    return  "anagram"   if sorted(s1) == sorted(s2) else "no anagram"

print(check_anagram("listen","silent"))
print(check_anagram("race","care"))
print(check_anagram("banana", "abanan"))
print(check_anagram("car","race"))

# output:
# anagram
# anagram
# anagram
# no anagram

"""

## 10. Find the longest word in a sentence

"""

# Find the longest word in a sentence

def find_longest_word_sentences(s):

    return max({i : len(i) for i in s.split(' ')},key = len )

print(find_longest_word_sentences("Python is an powerful programming language"))
print(find_longest_word_sentences("papa is good"))

# output:
# programming
# papa

def find_shortest_word_sentences(s):

    return min({i : len(i) for i in s.split(' ')},key = len )

print(find_shortest_word_sentences("Python is an powerful programming language"))
print(find_shortest_word_sentences("papa is good"))

# output:
# is
# is


"""
    ## 11. Remove thes spaces from a string.

"""

def remove_spaces_string(s):
    return s.replace(" ","")

print(remove_spaces_string("Python Developer"))
print(remove_spaces_string("Python is powerful programming language."))

"""
    ## 12. Find the most frequent character.

"""


def find_common_char_both(s,s1):

    return ' ' . join(set(s) & set(s1))

print(find_common_char_both("python","programming"))
print(find_common_char_both("hello",'her'))

# output:
# o n p
# h e

"""
    ## 13. find duplicate word in sentences.

"""

def find_duplicate_words(s):
    res = s.split(' ') 
    return '\n'.join({i for i in res if res.count(i)>1 })

print(find_duplicate_words("python java python sql java"))
print(find_duplicate_words("hello world hello"))

