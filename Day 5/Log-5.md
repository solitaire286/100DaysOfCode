## Topics covered

- Using the for loop with Python Lists
- for loops and the range() function

## Notes

- Loops allow us to execute the same line of code multiple times. [here](https://www.learnpython.org/en/Loops)
- **for** loops iterate over a given sequence. _(Note: Its good practice when writing loops to use the singular form of the list name it's referring to. E.g. brands = brand)_
- **for** loops can iterate over a sequence of numbers using the **range()** function.

```
lst1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# example 1:
for x in range(0, 10):
  print(x)

# example 2:
for x in range(0, len(lst1)):
  print(x)
```

- **sum()** function returns a number, the sum of all items in an iterable.

```
x = (1, 2, 3, 4, 5)

print(sum(x))
```

- **min(), max()** function returns the smallest and largest values in an iterable or in a series of regular arguments. [here](https://realpython.com/python-min-and-max/)

## Exercise & Project

- Average Height
- High Score
- Adding Even Numbers
- The FizzBuzz Job Interview Question
- Create a Password Generator

## Thoughts

Struggled a bit to wrap my head around the first exercise, where I had to calculate the total and count the number of all the elements within a list **without** using the sum() or len() functions.

Seems I overcomplicated it for myself by overthinking it, but I really appreciate how Angela manages to simplify each step in her solutions and explain it in a way which even a complete beginner could understand.

I believe this process of breaking things down and finding simple solutions for complicated problems will become easier as I write more code.

For now, I'm learning to read **for** loops as:

> For _**this element**_ in _**this list**_, run _**this block of code**_. _(Number of times looped = number of elements in the list or a given range.)_

Something Angela said about understanding the logic behind a function really stuck with me.

Python has many convenient functions which make math operations easier, but if you move to a different language and work on something else, then these might not exist.

> _"Understanding the underlying logic and being able to write out the code using things that every programming language has like the for loop will mean that you will become a much, much better programmer in the process."_

The Password Generator project wasn't as complicated as I had expected it to be. A few quick google searches, and I was able to complete it using **random.sample(), map()** and **join()**, all which were covered to some extent in prior lessons.

Alternatively, I still followed along with Angela's solution using **for** loops to randomly select, add/append elements from the provided lists into a new list/string, shuffle it and then print out the required result.

It's always good to learn more than just one way of doing something, and also to understand how to get a similar result if a certain function/method is not available, especially when working in another language.

It was a good experience, and I look forward to understanding these concepts better with more practice.

**Day 5 == Done!**
