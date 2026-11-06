import pickle


data = {"name": "John", "age": 30, "city": "New York"}

with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
    

with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file) 
print(loaded_data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}


# =================================================================================================================
# =================================================================================================================
# =================================================================================================================

""" 
We have a function that do some business logic and return square root of a nember. 
but we have to pass a number parameter instead list . so you have to handle proble.


"""

def calculate_the_square_root(num : int):
  
  return num**2


job_a = [1,3,2,4,6,5,7,8,9,10,11]

job_b = [calculate_the_square_root(i) for i in job_a]

print(job_b)


"""
    we have the string and we have to find the first non-repeating charcter in the string.
"""

def Find_first_non_repeating_charcter(char : str):
  repeat_count = {i:char.count(i) for i in char}
  # print(repeat_count)
  unique_count = [k for k,v in repeat_count.items() if v==1]
  return unique_count[0]
print(Find_first_non_repeating_charcter('swiss')) 


"""
    we have a list of numbers and we have to move all zeros in the list to the end of the list without 
    using second list or any sorting.

"""

def move_zero_to_end(arr):
    index = 0

    for i in range(len(arr)):
      if arr[i] !=0 :
        arr[index] = arr[i]
        index +=1
    for k in range(index,len(arr)):
      arr[k] = 0
    return arr


print(move_zero_to_end([1, 0, 2, 0, 3, 0]))
print(move_zero_to_end([0, 6, 4, 3, 0, 1]))
print(move_zero_to_end([0, 0, 1, 2]))

"""
    Reverse a string without using any inbuilt method.

"""
def string_rev_without_any_method(string :str):
  s = ''
  for i in range(len(string)-1,-1,-1):
    s+=string[i]

  return s

string = "Hello, World!"

print(string_rev_without_any_method(string))

"""
find the highest number in arr

"""

def sorted_list(arr : list):

  for i in range(len(arr)):
    for j in range(0,len(arr)-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]

  return arr

print(sorted_list([22,11,2,6,5,10,15,25,30,3,6]))

"""

    find the missing number in the list of n numbers.

"""

def find_missing_number(arr):
  n = len(arr)
  actual_num = n*(n+1)//2
  expected_num = sum(arr)
  return actual_num - expected_num

print(find_missing_number([3, 0, 1]))
print(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))


def two_sum(nums: list[int], target: int) -> list[int]:
    seen = []  # Value -> Index mapping
    for i in range(0,len(nums)):
      for j in range(i,len(nums)):
        if nums[i]+nums[j] == target:
          seen.append([i,j])
          
    return seen[0]

# Test:
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(two_sum([11, 15,8,1,6,2,3], 9)) 


"""
check if the given string has valid parentheses. The string can contain the characters '(', ')', '{', '}', '[' and ']'. A string is considered valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. An empty string is also considered valid.

"""

def check_valid_paranthisis(string : str):
  first_curly_check = [i for i in string if i == '{' ]
  second_curly_check = [j for j in string if j == '}']

  first_para_check = [i for i in string if i == '(' ]
  second_para_check = [j for j in string if j == ')']
  

  return True if (len(first_curly_check) == len(second_curly_check)) and (len(first_para_check) == len(second_para_check)) else False

print(check_valid_paranthisis("{{})}()"))
print(check_valid_paranthisis("{{})}(){}()"))
print(check_valid_paranthisis("{{})()"))
print(check_valid_paranthisis("{{}()}"))

"""
check if the given string has valid parentheses. The string can contain the characters '(', ')', '{', '}', '[' and ']'. A string is considered valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. An empty string is also considered valid.
"""

def check_valid_paranthisis(string : str):
  stack = []
  pairs = {
    ')' : '(',
    '}' : '{'
  }

  for ch in string :
    if ch in '({':
      stack.append(ch)
    elif ch in ')}':
      if not stack or stack[-1] != pairs[ch]:
        return False
      stack.pop()
  return len(stack) == 0

print(check_valid_paranthisis("{{})}()"))
print(check_valid_paranthisis("{{})}(){}()"))
print(check_valid_paranthisis("{{})()"))
print(check_valid_paranthisis("{}()"))

"""

    Given a string s, find the length of the longest substring without repeating characters.

"""

def longest_substring(s :str): 
  max_length = 0
  st =''
  for i in range(len(s)):
    temp = set()
    for j in range(i,len(s)):
      if s[j] in temp:
        break
      temp.add(s[j])
    max_length = max(max_length,len(temp))
  return max_length

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))

"""
    Given a string s, find the longest substring without repeating characters.

"""


def longest_substring(s :str): 
  max_string = ''
  st =''
  for i in range(len(s)):
    temp = ''
    for j in range(i,len(s)):
      if s[j] in temp:
        break
      temp +=s[j]
    if len(temp)>len(max_string):
      max_string = temp
  return max_string

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))

"""


"""



