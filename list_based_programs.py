
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