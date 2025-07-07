# A list is a mutable, ordered, and indexable collection of elements. Mutable means you can change its content after creation, ordered means the elements have a defined order, and indexable means you can access elements by their position (index).
# Lists can contain elements of different data types, including numbers, strings, and even other lists


# defining empty list
l0 = []  # An empty list
print(l0)  # Output: []


l1 = [1,"Ranajit",3.14,True,5]
# List slicing, the slice operator works similarly to string slicing, allowing you to access parts of the list.
# The syntax is the same as for strings: list[start:stop:step]
print(l1[0])  # Output: 1
print(l1[1:4])  # Output: ['Ranajit', 3.14, True] # from index 1 to 4 (not including 4)
print(l1[1:])  # Output: ['Ranajit', 3.14, True, 5] # from index 1 to the end
print(l1[:4])  # Output: [1, 'Ranajit', 3.14, True] # from the start to index 4 (not including 4)
print(l1[-1])  # Output: 5 (last element)
print(l1[-2])  # Output: True (second last element)
print(l1[-3:])  # Output: [3.14, True, 5] # from the third last element to the end
print(l1[-4:-1])  # Output: ['Ranajit', 3.14, True] # from the fourth last to the second last element
print(l1[1:4:2])  # Output: ['Ranajit', True] # from index 1 to 4 with step 2
print(l1[::])  # Output: [1, 'Ranajit', 3.14, True, 5] # entire list
x = l1[1:4:1]
print(x)  # Output: ['Ranajit', 3.14, True] # from index 1 to 4 with step 1, which is the same as l1[1:4]


# Mulability property of lists
l1[0] = 10  # Changing the first element
print(l1)  # Output: [10, 'Ranajit', 3.14, True, 5] # First element changed to 10

# nested lists
l2 = [1, 2, [3, 4], 5]  # A list containing another list
print(l2[2])  # Output: [3, 4] # Accessing
print(l2[2][0])  # Output: 3 # Accessing the first element of the nested list

# Build in methods for lists
l3 = [1, 2, 3, 4, 5]
# List concatenation
l4 = l3 + [6, 7, 8]  # Concatenating two lists
print(l4)  # Output: [1, 2, 3, 4, 5, 6, 7, 8] # Concatenated list
# List repetition
l5 = l3 * 2  # Repeating the list
print(l5)  # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] # Repeated list
# List length
print(len(l3))  # Output: 5 # Length of the list
# List membership
print(3 in l3)  # Output: True # Checks if 3 is in the list
print(10 in l3)  # Output: False # Checks if 10 is in the list
# List methods
print(l3.append(6))  # Appends 6 to the end of the list, returns None
print(l3)  # Output: [1, 2, 3, 4, 5, 6] # List after appending
print(l3.remove(2))  # Removes the first occurrence of 2 from the list, returns None
print(l3)  # Output: [1, 3, 4, 5, 6] # List after removing 2
print(l3.pop())  # Removes and returns the last element of the list, Output: 6
print(l3)  # Output: [1, 3, 4, 5] # List after popping the last element
print(l3.insert(1, 2))  # Inserts 2 at index 1
print(l3)  # Output: [1, 2, 3, 4, 5] # List after inserting 2 at index 1
print(l3.index(3))  # Output: 2 # Finds the index of the first occurrence of 3
print(l3.count(2))  # Output: 1 # Counts the occurrences of 2 in the list
print(l3.sort())  # Sorts the list in ascending order, returns None
print(l3)  # Output: [1, 2, 3, 4, 5] # List after sorting
# List reversal
l3.reverse()  # Reverses the list in place, returns None
print(l3)  # Output: [5, 4, 3, 2, 1] # List after reversing
# List copying
l6 = l3.copy()  # Creates a shallow copy of the list
print(l6)  # Output: [5, 4, 3, 2, 1] # Copy of the list
# List clearing
l3.clear()  # Removes all elements from the list, returns None
print(l3)  # Output: [] # List after clearing
# List comprehension
l7 = [x * 2 for x in range(5)]  # Creates a new list with elements doubled
print(l7)  # Output: [0, 2, 4, 6, 8] # List comprehension result
# List comprehension with condition
l8 = [x for x in range(10) if x % 2 == 0]  # Creates a new list with even numbers
print(l8)  # Output: [0, 2, 4, 6, 8] # List comprehension with condition
# List comprehension with nested loops
l9 = [x * y for x in range(3) for y in range(2)]  # Creates a new list with products
print(l9)  # Output: [0, 0, 0, 1, 0, 2] # List comprehension with nested loops, means x run for 0, 1, 2 and y run for 0, 1, so their is 2 * 3 = 6 elements in the list, and elements are calulates as x = 0 and y = 0, then x = 0 and y = 1, then x = 1 and y = 0, then x = 1 and y = 1, then x = 2 and y = 0, then x = 2 and y = 1
# List comprehension with nested lists
l10 = [[x, y] for x in range(3) for y in range(2)]  # Creates a new list with pairs
print(l10)  # Output: [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1]] # List comprehension with nested lists
# List comprehension with condition and nested loops
l11 = [x * y for x in range(3) for y in range(2) if x + y > 1]  # Creates a new list with products where sum is greater than 1
print(l11)  # Output: [2, 3, 4] # List comprehension with condition and nested loops
# List comprehension with filtering, filtering means it will create a new list with elements that satisfy the condition
l12 = [x for x in range(10) if x % 2 == 0 and x > 5]  # Creates a new list with even numbers greater than 5
print(l12)  # Output: [6, 8] 
# List comprehension with string manipulation
l13 = [char.upper() for char in "hello"]  # Creates a new list
print(l13)  # Output: ['H', 'E', 'L', 'L', 'O'] # List comprehension with string manipulation
# List comprehension with string manipulation and condition
l14 = [char for char in "hello" if char in "aeiou"]
print(l14)  # Output: ['e', 'o'] # List comprehension with string manipulation and condition
# List comprehension with string manipulation and condition
l15 = [char for char in "hello" if char not in "aeiou"]
print(l15)  # Output: ['h', 'l', 'l'] # List comprehension with string manipulation and condition
# List comprehension with string manipulation and condition
l16 = [char for char in "hello" if char.isalpha()]  # Creates a new list with alphabetic characters
print(l16)  # Output: ['h', 'e', 'l', 'l', 'o'] # List comprehension with string manipulation and condition
# list enumeration
l17 = ["apple", "banana", "cherry"]
for index, value in enumerate(l17):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: apple
# Index: 1, Value: banana
# Index: 2, Value: cherry
# List comprehension with enumeration
l18 = [f"{index}: {value}" for index, value in enumerate(l17)]
print(l18)  # Output: ['0: apple', '1: banana', '2: cherry'] # List comprehension with enumeration

# so the formating is :
#listname = [(expression(what is in the listname)) ((loops...)for item in iterable) if (conditions...(may use and or))]



# Tuple
# A tuple is an immutable, ordered, and indexable collection of elements. Immutable means you cannot change its content after creation, ordered means the elements have a defined order, and indexable means you can access elements by their position (index).
# Tuples can contain elements of different data types, including numbers, strings, and even other tuples
# defining empty tuple

t0 = ()  # An empty tuple
print(t0)  # Output: ()

t1 = (1, "Ranajit", 3.14, True, 5)
# Tuple slicing, the slice operator works similarly to string slicing, allowing you to access parts of the tuple.
# The syntax is the same as for strings: tuple[start:stop:step]
print(t1[0])  # Output: 1
print(t1[1:4])  # Output: ('Ranajit', 3.14, True) # from index 1 to 4 (not including 4)
print(t1[1:])  # Output: ('Ranajit', 3.14, True, 5) # from index 1 to the end
print(t1[:4])  # Output: (1, 'Ranajit', 3.14, True) # from the start to index 4 (not including 4)
print(t1[-1])  # Output: 5 (last element)
print(t1[-2])  # Output: True (second last element)
print(t1[-3:])  # Output: (3.14, True, 5) # from the third last element to the end
print(t1[-4:-1])  # Output: ('Ranajit', 3.14, True) # from the fourth last to the second last element
print(t1[1:4:2])  # Output: ('Ranajit', True) # from index 1 to 4 with step 2
print(t1[::])  # Output: (1, 'Ranajit', 3.14, True, 5) # entire tuple
x = t1[1:4:1]
print(x)  # Output: ('Ranajit', 3.14, True) # from index 1 to 4 with step 1, which is the same as t1[1:4]
# Immutability property of tuples
# t1[0] = 10  # This will raise a TypeError because tuples are immutable
# Nested tuples
t2 = (1, 2, (3, 4), 5)  # A tuple containing another tuple
print(t2[2])  # Output: (3, 4) # Accessing
print(t2[2][0])  # Output: 3 # Accessing the first element of the nested tuple
# Tuple concatenation
t3 = t2 + (6, 7, 8)  # Concatenating two tuples
print(t3)  # Output: (1, 2, (3, 4), 5, 6, 7, 8) # Concatenated tuple
# Tuple repetition
t4 = t2 * 2  # Repeating the tuple
print(t4)  # Output: (1, 2, (3, 4), 5, 1, 2, (3, 4), 5) # Repeated tuple
# Tuple length
print(len(t2))  # Output: 4 # Length of the tuple
# Tuple membership
print(3 in t2)  # Output: True # Checks if 3 is in the tuple
print(10 in t2)  # Output: False # Checks if 10 is in the tuple
# Tuple methods
# Tuples do not have methods like lists, but you can use built-in functions
print(t2.index(3))  # Output: 2 # Finds the index of the first occurrence of 3
print(t2.count(2))  # Output: 1 # Counts the occurrences of 2 in the tuple
# Tuple unpacking
a, b, (c, d), e = t2  # Unpacking the tuple into variables
print(a, b, c, d, e)  # Output: 1 2 3 4 5 # Unpacked values
# Tuple comprehension
# Tuples do not support comprehension like lists, but you can create a tuple using the tuple() function
t5 = tuple(x * 2 for x in range(5))  # Creates a new tuple with elements doubled
print(t5)  # Output: (0, 2, 4, 6, 8) # Tuple comprehension result
# Tuple comprehension with condition
t6 = tuple(x for x in range(10) if x % 2 == 0)  # Creates a new tuple with even numbers
print(t6)  # Output: (0, 2, 4, 6, 8) # Tuple comprehension with condition
# Tuple comprehension with nested loops
t7 = tuple(x * y for x in range(3) for y in range(2))  # Creates a new tuple with products
print(t7)  # Output: (0, 0, 0, 1, 0, 2) # Tuple comprehension with nested loops, means x run for 0, 1, 2 and y run for 0, 1, so their is 2 * 3 = 6 elements in the tuple, and elements are calulates as x = 0 and y = 0, then x = 0 and y = 1, then x = 1 and y = 0, then x = 1 and y = 1, then x = 2 and y = 0, then x = 2 and y = 1
# Tuple comprehension with nested tuples
t8 = tuple((x, y) for x in range(3) for y in range(2))  # Creates a new tuple with pairs
print(t8)  # Output: ((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)) # Tuple comprehension with nested tuples
# Tuple comprehension with condition and nested loops
t9 = tuple(x * y for x in range(3) for y in range(2) if x + y > 1)  # Creates a new tuple with products where sum is greater than 1
print(t9)  # Output: (2, 3, 4) # Tuple comprehension with condition and nested loops
# Tuple comprehension with filtering, filtering means it will create a new tuple with elements that satisfy the condition
t10 = tuple(x for x in range(10) if x % 2 == 0 and x > 5)  # Creates a new tuple with even numbers greater than 5
print(t10)  # Output: (6, 8)
# Tuple comprehension with string manipulation
t11 = tuple(char.upper() for char in "hello")  # Creates a new tuple
print(t11)  # Output: ('H', 'E', 'L', 'L', 'O') # Tuple comprehension with string manipulation
# Tuple comprehension with string manipulation and condition
t12 = tuple(char for char in "hello" if char in "aeiou")
print(t12)  # Output: ('e', 'o') # Tuple comprehension with string manipulation and condition
# Tuple comprehension with string manipulation and condition
t13 = tuple(char for char in "hello" if char not in "aeiou")
print(t13)  # Output: ('h', 'l', 'l') 
# Tuple comprehension with string manipulation and condition
t14 = tuple(char for char in "hello" if char.isalpha())  # Creates a new tuple with alphabetic characters
print(t14)  # Output: ('h', 'e', 'l', 'l', 'o') # Tuple comprehension with string manipulation and condition


'''
🔁 Difference Between Tuple and List in Python
| Feature               | Tuple                                  | List                                |
| --------------------- | -------------------------------------- | ----------------------------------- |
| **Definition**        | Ordered, immutable collection          | Ordered, mutable collection         |
| **Syntax**            | Defined using `()`                     | Defined using `[]`                  |
| **Mutability**        | ❌ Immutable – cannot be changed        | ✅ Mutable – elements can be changed |
| **Methods**           | Few (only `count()`, `index()`)        | Many (e.g., `append()`, `remove()`) |
| **Performance**       | Faster (less overhead)                 | Slightly slower                     |
| **Use Case**          | Fixed data, write-protected            | Dynamic data, needs modification    |
| **Memory Usage**      | Less memory                            | More memory                         |
| **Can be a dict key** | ✅ Yes (if elements are also immutable) | ❌ No (lists are unhashable)         |
'''
