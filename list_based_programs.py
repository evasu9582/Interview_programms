
"""
   ## 1. find largest numbers in list.
"""

def find_largest_number(lst):
    largest = lst[0]
    for i in lst:
      if i>largest:
        largest = i
    return largest

lst = [10,1,20,0,30,15]
print(find_largest_number(lst))

"""
    ## 2. find smallest numbers in list.

"""

def find_smallest_number(lst):
    smallest = lst[0]
    for i in lst:
      if i<smallest:
        smallest = i
    return smallest

lst = [10,1,20,30,15]
print(find_smallest_number(lst))

"""
## 3. find the second largest number in a list.

"""

a = [10, 20, 5, 40, 30]

b = sorted(set(a))

print(b[-2])

"""
## 4. find the second smallest number in a list.

"""

a = [10, 20, 5, 40, 30]

b = sorted(set(a))

print(b[1])

"""
## 5. reverse the list without any methods.

"""

def rev_list(lst):

    return lst[::-1]

print(rev_list([1,2,3,4,5,6]))

def rev_list1(lst):

    b = []
    for i in lst:
        b.insert(0,i)
    return b

print(rev_list1([1,2,3,4,5,6]))

def rev_without_any_method(lst):
    
    for i in range(0,len(lst)):
        for j in range(i, len(lst)):
            if lst[j]<lst[i]:
                lst[i],lst[j] = lst[j],lst[i]
    return lst

print(rev_without_any_method([7,6,8,9,1,3,5]))
print(rev_without_any_method([7,6,4,9,5,2,1,4]))

"""
## 6. find the missing number in a list.

"""

def missing_number(lst):

    n = max(lst)
    total = sum(range(min(lst),n+1))
    res = total - sum(lst)
    return res
    
print(missing_number([1,3,4]))
print(missing_number([5,6,9,8]))
print(missing_number([7,3,4,5,1,2,6]))


def missing_numbers(lst):

    return [i for i in range(min(lst),max(lst)+1) if i not in lst]

print(missing_numbers([1,3,4]))
print(missing_numbers([5,6,9,8]))
print(missing_numbers([7,3,4,5,1,2,6]))
print(missing_numbers([7,3,1]))
print(missing_numbers([2,1,7,5]))


"""
## 7. move zeros to the end of the list.

"""

def move_zeros_to_end(lst):
    index = 0
    for i in range(0,len(lst)):
      if lst[i] != 0:
          lst[index] = lst[i]
          index +=1

    for j in range(index,len(lst)):
        lst[j] = 0

    return lst
print(move_zeros_to_end([1,2,0,5,0,4,0]))
print(move_zeros_to_end([4,2,3,0,4,1,5,6,7]))
print(move_zeros_to_end([50,0,20,30,40,10,0,45,60,0]))

"""
    ## 8.find common items in two lists.
"""

def common_items_list(s,s1):

    return list(set(s) & set(s1))

print(common_items_list([4,5,2,3,1,6],[4,2,3,1,8,9]))
print(common_items_list([1,2,3,4],[3,4,5,6]))

"""
 ## 9. find uncommon items in two lists.
"""

def uncommon_items_list(s,s1):

    return list(set(s) ^ set(s1))

print(uncommon_items_list([4,5,2,3,1,6],[4,2,3,1,8,9]))
print(uncommon_items_list([1,2,3,4],[3,4,5,6]))

"""
## 10 . combine two lists .

"""

def combine_both_list(s,s1):

    return list(set(s) | set(s1))

print(combine_both_list([4,5,2,3,1,6],[4,2,3,1,8,9]))
print(combine_both_list([1,2,3,4],[3,4,5,6]))

def combine_lists(s,s1):
    return s + s1

print(combine_lists([4,5,2,3,1,6],[4,2,3,1,8,9]))
print(combine_lists([1,2,3,4],[3,4,5,6]))

"""
## 11. sort the list of tuples key value pair in the list.
"""

def sort_based_on_value(lst):
    
    return sorted(lst,key = lambda item : item[1])

print(sort_based_on_value([('a',7),('r',1),('b',8),('c',6)]))

"""
## 12.Rotate a list to the left by K positions

"""

def rotate_left(lst,k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate_left([1, 2, 3, 4, 5], 2)) # [3, 4, 5, 1, 2] 


"""
## 13. Rotate a list to the right by K positions.

"""

def rotate_right(lst,k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k] if k else lst[:]

print(rotate_right([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]


"""
## 14. sum of all numbers in a list.
"""

def sum_of_all_items(lst):
    total = 0
    for i in lst:
        total +=i
    return total
print(sum_of_all_items([2,4,1,5]))
print(sum_of_all_items([3,4]))
print(sum_of_all_items([2,4,3,1]))


"""
## 15. remove duplicates from a list without using set() methods or list methods

"""

def remove_duplicates_in_list(lst):

    l = []
    for i in lst:
      if i not in l:
        l.append(i)

    return l

print(remove_duplicates_in_list([2,1,2,3,1,4,5,4,6,5,7,0]))
print(remove_duplicates_in_list(2,2,3,3,1,1))

"""
## 16 . frequency of elements in a list.

"""

def frequency_of_list_items(lst):
    freq = {}
    for i in lst:
      if i not in freq:
        freq[i] =1
      else:
        freq[i] += 1
    return freq

print(frequency_of_list_items([1,2,1,2,3,4,5,6]))

"""
## 17. merge the two lists.
"""

def merge_two_list(a,b):
    return a + b

print(merge_two_list([1,2],[3,4]))
print(merge_two_list([0,1],[10,4]))

"""
## 18. Find pairs whose sum equals a target
"""

def find_targets_equals_to_target(lst,target):

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] + lst [j] == target:
                print(lst[i] , lst[j])

a = [2, 4, 3, 5, 7, 8]
target = 10

find_targets_equals_to_target(a,target)
print(" ")
find_targets_equals_to_target([4,2,1,4,3,5,6,7],8)

"""
## 19. find the maximum difference between two elements in a list such that larger element appears after the smaller number.
"""

def max_diff_between_two_elem(lst):

    min_value = lst[0]
    max_diff = 0
    
    for i in lst[1:]:
        max_diff = max(max_diff, i - min_value)
        min_value = min(min_value, i)
    return max_diff

print(max_diff_between_two_elem([2, 3, 10, 6, 4, 8, 1]))

"""
20. find the largest consecutive number in a list
"""


def largest_consecutive_number(lst):
    a = list(set(lst))
    a.sort()
    # print(a)
    largest_freq = min(a)
    for i in range(len(a)-1):
      # print(a[i+1]- a[i])
      if a[i+1] - a[i] == 1:
        largest_freq = a[i+1]
      else:
        break
    return largest_freq
print(largest_consecutive_number([100,1,20,2,3,30]))
print(largest_consecutive_number([0,3,2,1,10,7,8,4]))
print(largest_consecutive_number([0,4,1,5]))
# print(diff)

"""
21 . flatten a list of lists into a single list.
"""

def flatten_list(lst):
    return [j for i in lst for j in i]

print(flatten_list([[1, 2], [3, 4], [5, 6]]))

"""
22. find the subarrays based on targets.
"""

def subarray_list(lst,target):

    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
          sub = lst[i:j]
          if sum(sub) == target:
              print(sub)

subarray_list([1, 2, 3, 4],5)
print(" ")
subarray_list([1, 2, 3, 4,3,1,9,3,5],7)
