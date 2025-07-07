# Dictionary is a collection of key-value pairs.
# A set is a collection of unique elements.
# Dictionarys are mutable, unordered, and indexed by keys.

my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing dictionary values
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 30
print(my_dict.get("country", "USA"))  # Output: USA (default value if key not found) the format of the get method is get(key, default_value)
#  the difference between get and [] is that get will not raise an error if the key is not found, it will return None or the default value if provided

# Adding a new key-value pair
my_dict["country"] = "USA"
# Updating an existing key-value pair
my_dict["age"] = 31
# Deleting a key-value pair
del my_dict["city"]
# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary")  # Output: Name exists in the dictionary
# Iterating through keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: Alice
# age: 31
# country: USA

# Dictionary methods
print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'country'])
print(my_dict.values())  # Output: dict_values(['Alice', 31, 'USA'])
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 31), ('country', 'USA')])
# this 3 methods always return a view object, which is a dynamic view on the dictionary’s entries, meaning that when the dictionary changes, the view reflects these changes.
# Copying a dictionary
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

# Merging dictionaries
another_dict = {"city": "Los Angeles", "occupation": "Engineer"}
my_dict.update(another_dict)
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA', 'city': 'Los Angeles', 'occupation': 'Engineer'}
# Dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}





# Set is a collection of unique elements.
# A mutable, unordered collection of unique items.
# Defined with curly braces {} or set() constructor.
# Cannot contain mutable items (like lists).
# Sets are useful for membership testing, removing duplicates, and performing mathematical operations like union, intersection, and difference.
# There is no way to change items in sets.

# defining empty set
my_set = set()  # or my_set = {}
# defining a set with elements
my_set = {1, 2, 3, 4, 5}
# Adding elements to a set
my_set.add(6)
# Removing elements from a set
my_set.remove(3)  # Raises KeyError if the element is not found
my_set.discard(7)  # Does not raise an error if the element is not found
# print(my_set[1]) # Raises TypeError: 'set' object is not subscriptable (sets do not support indexing)
# Checking if an element exists in a set
if 2 in my_set:
    print("2 is in the set")  # Output: 2 is in the set
# Iterating through a set
for item in my_set:
    print(item)
# Output:
# 1
# 2
# 4
# 5
# Set methods
print(my_set.union({7, 8}))  # Output: {1, 2, 4, 5, 6, 7, 8}
print(my_set.intersection({2, 4, 6}))  # Output: {2, 4, 6}
print(my_set.difference({1, 2, 3}))  # Output: {4, 5, 6}
print(my_set.isdisjoint({7, 8}))  # Output: True (no common elements)
print(my_set.issubset({1, 2, 3, 4, 5, 6}))  # Output: True (my_set is a subset of the larger set)
print(my_set.issuperset({2, 4}))  # Output: True (my_set contains all elements of the smaller set)
# Set comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set)  # Output: {0, 1, 4, 9, 16}
# Converting a list to a set to remove duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]
my_unique_set = set(my_list)
print(my_unique_set)  # Output: {1, 2, 3, 4, 5} (duplicates removed)
# Converting a set to a list
my_set_list = list(my_set)
print(my_set_list)  # Output: [1, 2, 4, 5, 6] (order may vary since sets are unordered)
# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
# Union
union_set = set_a | set_b
print(union_set)  # Output: {1, 2, 3, 4, 5}
# Intersection
intersection_set = set_a & set_b
print(intersection_set)  # Output: {3}
# Difference
difference_set = set_a - set_b
print(difference_set)  # Output: {1, 2}
# Symmetric Difference
symmetric_difference_set = set_a ^ set_b
print(symmetric_difference_set)  # Output: {1, 2, 4, 5} (elements in either set but not both)
# Frozen Set: Immutable version of a set
frozen_set = frozenset([1, 2, 3])
print(frozen_set)  # Output: frozenset({1, 2, 3})
# Attempting to add an element to a frozen set will raise an AttributeError
# frozen_set.add(4)  # Raises AttributeError: 'frozenset' object has no attribute 'add'
# Frozen sets can be used as dictionary keys or set elements
my_frozen_set = frozenset(my_set)
print(my_frozen_set)  # Output: frozenset({1, 2, 4, 5, 6})
# Using sets for mathematical operations
# Sets can be used to perform mathematical operations like union, intersection, and difference.
# These operations are useful for tasks like finding common elements, unique elements, or differences between datasets.
'''
🔁 List vs Set
| Feature        | List                          | Set                          |
| -------------- | ----------------------------- | ---------------------------- |
| **Order**      | Ordered                       | Unordered                    |
| **Duplicates** | Allows duplicates             | Does not allow duplicates    |
| **Indexing**   | Supports indexing (`list[0]`) | Does not support indexing    |
| **Mutable**    | Yes                           | Yes                          |
| **Defined by** | Square brackets `[]`          | Curly braces `{}` or `set()` |
| **Use case**   | Ordered collection            | Unique, unordered collection |

📁 Dictionary vs Set
| Feature        | Dictionary                  | Set                          |
| -------------- | --------------------------- | ---------------------------- |
| **Structure**  | Key-value pairs             | Only values (no keys)        |
| **Duplicates** | Keys must be unique         | All items must be unique     |
| **Indexing**   | Access by key               | No direct access by index    |
| **Mutable**    | Yes                         | Yes                          |
| **Defined by** | Curly braces `{key: value}` | Curly braces `{}` or `set()` |
| **Use case**   | Store data with labels      | Store unique items           |

📄 Dictionary vs List
| Feature                 | Dictionary                      | List                        |
| ----------------------- | ------------------------------- | --------------------------- |
| **Structure**           | Key-value pairs                 | Sequence of values          |
| **Access**              | By key                          | By index                    |
| **Order (Python 3.7+)** | Maintains insertion order       | Maintains order             |
| **Duplicates**          | Keys must be unique             | Allows duplicates           |
| **Defined by**          | `{}` with key-value pairs       | `[]` with elements          |
| **Use case**            | Structured data (like a record) | Ordered collection of items |

'''