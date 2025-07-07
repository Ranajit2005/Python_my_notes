#How to create a string in Python

a = 'Ranajit'
b = "Ranjit"
c = '''Ranjit'''
d = """Ranjit"""

sen = "This is a multi-line string."

# String is immutable, meaning once created, it cannot be changed.
# However, you can create a new string based on the original one.

# Stirng slicing
print(a[0])  # Output: R
print(a[1:4])  # Output: ana , # from index 1 to 4 (not including 4)
print(a[1:])  # Output: anajit , # from index 1 to the end
print(a[:4])  # Output: Rana # from the start to index 4 (not including 4)
print(a[-1])  # Output: t (last character)
print(a[-2])  # Output: i (second last character)
print(a[-3:])  # Output: jit (last three characters) , # from the third last character to the end
print(a[-4:-1])  # Output: naj (from the fourth last to the second last character)
print(a[1:4:2])  # Output: an (from index 1 to 4 with step 2)
print(a[::])  # Output: Ranajit (entire string)
x = a[1:4:1]
print(x)  # Output: ana (from index 1 to 4 with step 1), # which is the same as a[1:4]
y = "qwertyuiopasdfghjklzxcvbnm"  # ******************************************* VVI 
print(y[1::3]) # means it will print every third character starting from index 1
print(a[::-1])  # Output: tijnaR (reversed string)
print(a[::-2])  # Output: tjnaR (every second character in reverse)

# String concatenation
print(a + b)  # Output: RanajitRanjit (concatenation of two strings)
print(a + " " + b)  # Output: Ranajit Ranjit (concatenation with a space in between)

# String repetition
print(a * 3)  # Output: RanajitRanajitRanajit

# String length
print(len(a))  # Output: 7 (length of the string 'Ranajit')

# String membership
print('R' in a)  # Output: True (checks if 'R' is in 'Ranajit')
print('x' in a)  # Output: False (checks if 'x' is in 'Ranajit')

# String methods
print(a.upper())  # Output: RANAJIT (converts to uppercase)
print(a.lower())  # Output: ranajit (converts to lowercase)
print(a.title())  # Output: Ranajit (capitalizes the first letter of each word)
print(a.capitalize())  # Output: Ranajit (capitalizes the first letter)
print(a.strip())  # Output: Ranajit (removes leading and trailing whitespace)
print(a.replace('R', 'J'))  # Output: Janajit (replaces 'R' with 'J')
print(a.split('a'))  # Output: ['R', 'najit'] (splits the string at 'a')
print(a.find('a'))  # Output: 1 (finds the first occurrence of 'a')
print(a.index('a'))  # Output: 1 (finds the first occurrence of 'a', raises ValueError if not found)


c = "hello"

print(c.find('l'))   # Output: 2
print(c.index('l'))  # Output: 2

print(c.find('z'))   # Output: -1
print(c.index('z'))  # Error: ValueError: substring not found



print(a.count('a'))  # Output: 2 (counts occurrences of 'a')
print(a.startswith('R'))  # Output: True (checks if the string starts with 'R')
print(a.endswith('t'))  # Output: True (checks if the string ends with 't')
print(a.isalpha())  # Output: True (checks if all characters are alphabetic)
print(a.isdigit())  # Output: False (checks if all characters are digits)
print(a.isalnum())  # Output: True (checks if all characters are alphanumeric)
print(a.islower())  # Output: False (checks if all characters are lowercase)
print(a.isupper())  # Output: False (checks if all characters are uppercase)
print(a.isspace())  # Output: False (checks if all characters are whitespace)
print(a.swapcase())  # Output: rANAJIT (swaps case of each
# character)
print(a.center(20, '*'))  # Output: ****Ranajit**** (centers the string in a field of width 20, filling with '*')
print(a.ljust(20, '-'))  # Output: Ranajit---------- (left-justifies the string in a field of width 20, filling with '-')
print(a.rjust(20, '-'))  # Output: ----------Ranajit (right-justifies the string in a field of width 20, filling with '-')
print(a.zfill(10))  # Output: 0000Ranajit (pads the string with zeros on the left to make it 10 characters long)
print(a.partition('a'))  # Output: ('R', 'a', 'najit') (partitions the string at the first occurrence of 'a')
print(a.rpartition('a'))  # Output: ('Ranjit', 'a', '') (partitions the string at the last occurrence of 'a')
print(a.splitlines())  # Output: ['Ranajit'] (splits the string into lines, useful for multi-line strings)
print(a.join(['Hello', 'World']))  # Output: HelloRanajitWorld (joins the list of strings with 'Ranajit' as the separator)
# String formatting
name = "Ranjit"
age = 25
# Using f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Ranjit and I am 25 years old.
# Using format method
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is Ranjit and I am 25 years old.
# Using % operator
print("My name is %s and I am %d years old." % (name, age))  # Output: My name is Ranjit and I am 25 years old.
# String interpolation
print("My name is %s and I am %d years old." % (name, age))  # Output: My name is Ranjit and I am 25 years old.
# String encoding and decoding
# Encoding a string to bytes
encoded_str = a.encode('utf-8')  # Converts the string to bytes using UTF-8 encoding
print(encoded_str)  # Output: b'Ranajit' (bytes representation)
# Decoding bytes back to a string
decoded_str = encoded_str.decode('utf-8')  # Converts bytes back to string using
# UTF-8 decoding
print(decoded_str)  # Output: Ranajit (original string)
# String comparison
str1 = "apple"
str2 = "banana"
print(str1 < str2)  # Output: True (compares lexicographically)
print(str1 > str2)  # Output: False (compares lexicographically)
print(str1 == str2)  # Output: False (checks for equality)
print(str1 != str2)  # Output: True (checks for inequality)

