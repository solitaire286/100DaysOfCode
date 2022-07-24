## Topics covered

- Primitive Data Types
- Type Error, Type Checking and Type Conversion
- Mathematical Operations
- Number Manipulation and f-Strings

## Notes

Introduction to primitive data types in python. (Strings, Integers, Floats and Booleans)
Subscripting: The use of [] to index the position of a character from within a string.
Improving the readability of large numbers within the codebase by using underscores. (E.g. 123_456_789 = 123,456,789)
Using the type check function (type) to check data type.
Type Conversion / Type Casting: Converting one type of data into another.

When you have multiple math operations in the same line of code it will follow the PEMDAS rule on priority.

PEMDAS (Based on it's priority the operations are always executed from left to right)

Parenthesis
Exponents (raise to the power of)
Multiplication
Division
Addition
Subtraction

<!-- prettier-ignore -->
Isolate certain calculations using '(parenthesis)' to elevate it's priority on the list. E.g. print(3 * (3 + 3) / 3 - 3)

Use the 'round()' function or 'floor division //' to round off decimal numbers. E.g print(round(8 / 3, 2))

When having to manipulate the value of a variable based on it's previous value, use shorthand instead of repeating the same.

E.g. score = 1, instead of writing 'score = score + 1', we can use 'score += 1'

fStrings are used to convert multiple data types into string types instead of having to manually convert each one separately.

E.g. print(f"You are {weight} kilos and {height}m tall. You play football is {True}")

## Project

- BMI Calculator
- Life in Weeks
- Tip Calculator

## Thoughts

BMI Calculator exercise was fun. Actually got to utilize most of the concepts we covered so far. (Variables, Type Checking, Type Conversion, Math Operations)
