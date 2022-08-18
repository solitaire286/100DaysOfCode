## Topics covered

- Defining and Calling Python Functions
- Indentation in Python
- While Loops

Functions, Code Blocks and While Loops

## Notes

- Functions are a block of statements that return the specific task. Its convenient to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
- Built-in Functions (Python) [here](https://docs.python.org/3/library/functions.html)
- Create a python function using the **def** (define) keyword. After creating a function we can call it by using the name of the function followed by parenthesis containing parameters of that particular function.

```
# Define function.
def hello():
  print("Hello World!")

# Call function.
hello()
```

- **while** loops repeat as long as a certain boolean condition is met.

```
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1

# Written in its negation to read; while count is 'not' greater than 5

count = 0
while not count > 5:
    print(count)
    count += 1
```

-
-

## Exercise & Project

- The Hurdles Loop Challenge
- Hurdles Challenge using While Loops
- Jumping over Hurdles with Variable Heights
- Escaping the Maze

## Thoughts

**When to use a for loop? And when to use a while loop?**

> Use for loops when you want to iterate over something, and you need to do something with each item that you are iterating over.
>
> i.e. If you're iterating through a list and for each item on that list you want to be able to do something with each of these items.
>
> Or use the range function to iterate over a number of times within a specific range.
>
> Use while loops when you don't really care what number in a sequence you're in, which item you're iterating through in a list, and you just simply want to carry out some sort of functionality many, many times until some sort of condition that you set is either true or false.

**Infinite Loops**

> While loops are a little bit more dangerous than for loops because in for loops, you're setting ahead of time how many times something is going to run. It's going to stop once it reaches the end of the list of items or once it reaches the upper bounds of a given range.
>
> But for while loops, they will continue running until a particular condition switches to false. So if you have some sort of condition that actually never becomes false, well then your while loop becomes something known as an infinite loop.
>
> Often times it's really helpful when you don't know why you're getting an infinite loop to simply just print out your condition.
