
"""
## 1. Find the even numbers or odd number in give number.

"""

def check_even_or_odd_num(n):

    return "Even Number" if n%2 == 0 else 'Odd Number'

print(check_even_or_odd_num(3))
print(check_even_or_odd_num(4))
print(check_even_or_odd_num(5))
print(check_even_or_odd_num(12))


"""
## 2. sum of given number.

"""

def sum_of_number(n):
  total = 0
  while n > 0:
    total += n%10
    n//=10
  return total
print(sum_of_number(18))

# output:
# 9

"""
## 3. Reverse the given number.

"""

def reverse_number(n):
      rev = 0
      while n > 0:
        rev = rev * 10 + n % 10
        n //=10
      return rev

print(reverse_number(123))
print(reverse_number(12))
print(reverse_number(2))

"""
 ## 4. Check the given number is palindrome or not.
"""

def palindrome_number(n):
    temp = n
    rev = 0
    while n > 0:
      rev = rev * 10 + n % 10
      n //=10

    return "it is palindrome number" if rev == temp else "It is not the palindrome number"

print(palindrome_number(121))
print(palindrome_number(123))
print(palindrome_number(1001))
print(palindrome_number(10))

"""
    ## 5. Count of digits in a number.
"""

def count_of_digits_in_number(n):
    return len(str(abs(n)))

print(count_of_digits_in_number(123))
print(count_of_digits_in_number(12))

"""

    ## 6. count of even and odd numbers in number.

"""

def find_even_odd_count_number(n):
      even = odd = 0
      while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        n //=10
      return (even , odd)

print(find_even_odd_count_number(1467892))
print(find_even_odd_count_number(123456))

"""
## 7. finding a largest digit in a number.

"""

def find_largest_digit(n):
    largest = 0
    while n>0:
      largest = max(largest,n%10)
      n //= 10
    return largest

print(find_largest_digit(58321))
print(find_largest_digit(563237))
print(find_largest_digit(78910))
print(find_largest_digit(10213141516171819))

"""
 ## 8. finding a smallest digit in a number.
"""

def find_smallest_digit(n):
    smallest = 2
    while n> 0:
      smallest = min(smallest,n%10)
      n //= 10
    return smallest

print(find_smallest_digit(58321))
print(find_smallest_digit(563237))
print(find_smallest_digit(78910))
print(find_smallest_digit(10213141516171819))

"""
## 9. Product of digits in a number.
"""

def product_of_digits(n):
    product = 1
    while n >0 :
        product *= n % 10
        n //=10
    return product 

print(product_of_digits(234)) #24 = 2*3*4
print(product_of_digits(123)) #6 = 1*2*3    
print(product_of_digits(101)) #0 = 1*0*1
print(product_of_digits(11)) #1 = 1*1
print(product_of_digits(42)) #8 = 4*2
print(product_of_digits(198)) #162 = 1*9*8

"""
## 10. Count the frequency of each digit in a number.
"""

def frequency_of_digits(n):
    s = str(abs(n))

    for k in s:
      print(f"count of {k} :",s.count(k))
# frequency_of_digits(123)
frequency_of_digits(4477906)

"""
## remove zero from a number.

"""

def remove_zero_from_number(n):
    s = str(abs(n))
    res = s.replace('0',"")
    return int(res)

print(remove_zero_from_number(102030))
print(remove_zero_from_number(120300419))
print(remove_zero_from_number(304050897))

"""
## Armstong number or not.
"""


def armstrong_number(n):
    num = sum([int(i)**len(str(n)) for i in str(abs(n))])

    return num == n

print(armstrong_number(153))

