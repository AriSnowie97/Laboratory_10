def factorial_recursive(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def fibonacci_recursive(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        return "Fibonacci sequence is not defined for negative indices."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def sum_list_recursive(data_list):
    if not isinstance(data_list, list):
        raise TypeError("Input must be a list.")
    if not data_list:
        return 0
    else:
        return data_list[0] + sum_list_recursive(data_list[1:])

def is_palindrome_recursive(text):
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    processed_text = ''.join(filter(str.isalnum, text)).lower()
    n = len(processed_text)

    if n <= 1:
        return True
    elif processed_text[0] == processed_text[-1]:
        return is_palindrome_recursive(processed_text[1:-1])
    else:
        return False

if __name__ == "__main__":
    # Test factorial_recursive
    print("Factorial Recursive:")
    print(f"Factorial of 5: {factorial_recursive(5)}")
    print(f"Factorial of 0: {factorial_recursive(0)}")
    print(f"Factorial of -1: {factorial_recursive(-1)}")
    try:
        print(f"Factorial of 'a': {factorial_recursive('a')}")
    except TypeError as e:
        print(f"Error: {e}")

    # Test fibonacci_recursive
    print("\nFibonacci Recursive:")
    print(f"Fibonacci(6): {fibonacci_recursive(6)}")
    print(f"Fibonacci(0): {fibonacci_recursive(0)}")
    print(f"Fibonacci(1): {fibonacci_recursive(1)}")
    print(f"Fibonacci(-2): {fibonacci_recursive(-2)}")
    try:
        print(f"Fibonacci of 3.5: {fibonacci_recursive(3.5)}")
    except TypeError as e:
        print(f"Error: {e}")

    # Test sum_list_recursive
    print("\nSum List Recursive:")
    print(f"Sum of [1, 2, 3, 4, 5]: {sum_list_recursive([1, 2, 3, 4, 5])}")
    print(f"Sum of []: {sum_list_recursive([])}")
    try:
        print(f"Sum of 'hello': {sum_list_recursive('hello')}")
    except TypeError as e:
        print(f"Error: {e}")

    # Test is_palindrome_recursive
    print("\nIs Palindrome Recursive:")
    print(f"Is 'racecar' a palindrome? {is_palindrome_recursive('racecar')}")
    print(f"Is 'A man, a plan, a canal: Panama' a palindrome? {is_palindrome_recursive('A man, a plan, a canal: Panama')}")
    print(f"Is 'hello' a palindrome? {is_palindrome_recursive('hello')}")
    print(f"Is '': {is_palindrome_recursive('')}")
    try:
        print(f"Is 121 a palindrome? {is_palindrome_recursive(121)}")
    except TypeError as e:
        print(f"Error: {e}")
