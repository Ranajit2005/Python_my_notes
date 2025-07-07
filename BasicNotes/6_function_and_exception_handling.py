# function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Functions are defined using the def keyword.


# Function definition
def greet(name):
    return f"Hello, {name}!"
greeted_message = greet("Alice")
print(greeted_message)  # Output: Hello, Alice!

# Function with default parameter
def greet_with_default(name="Guest"):
    return f"Hello, {name}!"
greeted_message_default = greet_with_default()
print(greeted_message_default)  # Output: Hello, Guest!
# Function with multiple parameters
def add_numbers(a, b):
    return a + b
sum_result = add_numbers(5, 10)
print(sum_result)  # Output: 15
# Function with variable number of arguments
def sum_all(*args):
    return sum(args)
sum_result_all = sum_all(1, 2, 3, 4, 5)
print(sum_result_all)  # Output: 15
# Function with keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
# Function with return statement
def multiply(a, b):
    return a * b
product_result = multiply(3, 4)
print(product_result)  # Output: 12
# Function with no return statement
def print_message(message):
    print(message)
print_message("This is a message.")  # Output: This is a message.

def pass_function():
    pass  # This function does nothing and is used as a placeholder.
# Function with a docstring
def example_function():
    return "This function does something."
print(example_function.__doc__)  # Output: This is an example function with a docstring.
# lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25



# Exception handling lets you handle errors (like dividing by zero, invalid input, file not found, etc.) without stopping the whole program.

# Basic try-except block
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    print(f"Error: {e}")
# Output: Error: division by zero

# Catching multiple exceptions
try:
    value = int("abc")  # This will raise a ValueError
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
# Output: Error: invalid literal for int() with base 10: 'abc'

# Finally block
try:
    file = open("non_existent_file.txt", "r")  # This will raise a FileNotFoundError
except FileNotFoundError as e:
    print(f"Error: {e}")
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")
# Output: This block always executes, regardless of whether an exception occurred or not.
# Output: Error: [Errno 2] No such file or directory: 'non_existent_file.txt'
# Raising exceptions

# Now we can see, finally block is always executed, even if an exception occurs. So we can write the code as usual, and the code of finally block write after the try-except block. So what is the use of finally block? We can see it in function

def check1(num1,num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return e
    print("The code after return statement will not be executed.")
check1_result = check1(10, 0)
print(check1_result)  # Output: Error: division by zero
# Now if I write the last line of the function after the return statement, it will not be executed. So we can use finally block to execute the code after try-except block.
def check2(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return e
    finally:
        print("This block always executes, regardless of whether an exception occurred or not.")
check2_result = check2(10, 0)
print(check2_result)  # Output: Error: division by zero
# Output: This block always executes, regardless of whether an exception occurred or not.
    
# So now it will execute the code after return statemant in finally block, even if an exception occurs. So we can use finally block to execute the code after try-except block.


# Custom exception
class CustomError(Exception):
    pass
try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"Custom Error: {e}")
# Output: Custom Error: This is a custom error

# multiple exception Handling in Python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("Some error occurred:", e)

'''
⚠️ Common Python Exceptions
| Exception           | Description                                                    | Example                           |
| ------------------- | -------------------------------------------------------------- | --------------------------------- |
| `ZeroDivisionError` | Raised when dividing by zero                                   | `10 / 0`                          |
| `ValueError`        | Raised when a function receives the right type but wrong value | `int("abc")`                      |
| `TypeError`         | Raised when an operation is applied to an inappropriate type   | `len(5)`                          |
| `IndexError`        | Accessing an index that is out of range                        | `[1, 2][5]`                       |
| `KeyError`          | Accessing a non-existent dictionary key                        | `{"a": 1}["b"]`                   |
| `NameError`         | Using a variable that hasn't been defined                      | `print(x)` (if `x` isn't defined) |
| `AttributeError`    | Accessing an undefined method or attribute                     | `"abc".push()`                    |
| `FileNotFoundError` | Trying to open a file that doesn’t exist                       | `open("nofile.txt")`              |
| `ImportError`       | Error in importing a module                                    | `import non_existent_module`      |
| `IndentationError`  | Incorrect indentation in code                                  | (wrong spacing in block)          |
| `SyntaxError`       | Invalid syntax                                                 | `print("Hello"` (missing `)`)     |
| `RuntimeError`      | A generic error not caught by other exceptions                 | Custom runtime issues             |
| `StopIteration`     | Raised by `next()` when iterator is exhausted                  | `next(iter([]))`                  |
| `MemoryError`       | When the program runs out of memory                            | Huge list or recursion            |
'''

