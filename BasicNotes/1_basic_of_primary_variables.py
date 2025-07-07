print("Hellow World")

# Try single line comment
'''
This is a multi-line comment
It can span multiple lines
This is useful for documentation or explanations
'''



# Primary data type in python, they are basically 5 types ->
# Integer
x = 5
# Float
y = 3.14
# String
name = "John Doe"
# Boolean
is_active = True
# NoneType
nothing = None

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(name))  # Output: <class 'str'>
print(type(is_active))  # Output: <class 'bool'>
print(type(nothing))  # Output: <class 'NoneType'>



# typecasting
x_str = str(x)  # Convert integer to string
y_int = int(y)  # Convert float to integer
print(x_str)  # Output: '5'
print(y_int)  # Output: 3 , # Note: This truncates the decimal part

a = "Ranjit"

# b = int(a)  # This will raise an error because 'Ranjit' cannot be converted to an integer, ValueError: invalid literal for int() with base 10: 'Ranjit'
# print(b)  # This line will not be executed due to the error above



# taking input from user
user_name = input("Enter your name: ") # it always takes input as string
user_age = int(input("Enter your age: "))  # Convert input to integer

print(f"Hello, {user_name}! You are {user_age} years old.")
