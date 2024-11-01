# UTF-8 Validation Module

This module provides a function to validate if a list of integers represents valid UTF-8 codepoints. It checks the encoding according to the UTF-8 standard and returns `True` if the data is valid, otherwise it returns `False`.

## Usage

To use the `validUTF8` function, simply pass a list of integers as an argument.

Example:
# Example usage of the validUTF8 function
data1 = [197, 130, 1]  # Valid UTF-8
data2 = [235, 140, 4]  # Invalid UTF-8

print(validUTF8(data1))  # Output: True
print(validUTF8(data2))  # Output: False
