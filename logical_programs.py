def sort_by_value(arr):
    return sorted(arr.items(), key=lambda item: item[1])


if __name__ == "__main__":
    dct = {'naveen': 33, 'Harish': 33, 'vasu': 32, 'syed': 33}
    print(sort_by_value(dct))


def recursive_access(data):
    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, dict):
                result = recursive_access(value)
                if result is not None:
                    return result
            elif value == 'vasu':
                return value

        if 'name' in data:
            return data['name']

    return None


data = {'a': {'b': 1, 'c': {'d': 2, 'e': {'name': 'vasu'}}}}
print(recursive_access(data))

# Fibonacci series

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


fibonacci(10)

# Prime numbers

def prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print("\n")
print(prime_numbers(20))


# input : aabbbccccddde
# output : a2b3c4d3e

from itertools import groupby

def compress_string(s):
    compressed = []
    for char, group in groupby(s):
        count = len(list(group))
        compressed.append(f"{char}{count}" if count > 1 else char)
    return ''.join(compressed)

compressed_string = compress_string("aabbbccccddde")
print(compressed_string)

# bubble sort in simple way

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
bubble_sorted_array = bubble_sort([64, 34, 25, 12, 22, 11, 90])
print(bubble_sorted_array)

# binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_array = [11, 12, 22, 25, 34, 64, 90]
target = 25
result = binary_search(sorted_array, target)
print(f"Element found at index: {result}")

# sort two names and check whether they match

name1 = "emme"
name2 = "ememe"

sorted_name1 = ''.join(sorted(name1))
sorted_name2 = ''.join(sorted(name2))

print(f"Sorted name1: {sorted_name1}")
print(f"Sorted name2: {sorted_name2}")

if sorted_name1 == sorted_name2:
    print("Matched")
else:
    print("Not Matched")