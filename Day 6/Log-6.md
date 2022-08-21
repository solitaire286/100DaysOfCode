## Topics covered

- Defining and Calling Python Functions
- Indentation in Python
- While Loops

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

## Exercise & Project

- The Hurdles Loop Challenge
- Hurdles Challenge using While Loops
- Jumping over Hurdles with Variable Heights
- Escaping the Maze

## Thoughts

It has been challenging to maintain a proper cadence in completing a single day of the course without stretching it over multiple days.

With a full 9-hour work shift, 3-4 hours of scheduled power outages daily during my waking hours means very little time to actually complete all the topics, exercises, and project in a day. And pulling from the 4-5 hours of sleep means my productivity, health, and concentration take a hit.

Even Angela mentioned it might take more than a day to complete a single day's module, which is expected. But having it take up to 2-3 days due to external factors is frustrating. 😔

Still, I'm sure in the grand scheme of things, this will be worth it. Taking the time to get the basics right without rushing through them for the sake of completing a "Day". Putting more effort into writing more code and notes so I can understand these concepts better will definitely improve my knowledge and efficiency in the future.

Using Reeborg's world _(Karel)_ is a fun way to practice, understand and visualize things when getting started with defining basic functions, using while loops and conditionals to test and iterate the code when the program is run.

The initial 4 challenges of the day were quite straightforward, but the final maze challenge is where I struggled most. Spent a good 4-5 hours trying to get it to pass on each scenario but alas, I realized I was spending too much time on this one problem, when at this point of the learning process its best to move on and return to it once I have more experience and knowledge.

Oddly enough, when I watched Angela's solution even she couldn't get the challenge to pass on every scenario and said this is a problem you should revisit once you're at a more intermediate level. It was relieving to hear that and I will definitely come back and solve this in the future.

As usual, I ended up overthinking and overcomplicating things for myself while Angela's code was very simple and straightforward.

This is definitely something I need to work on. Being able to break down problems and write code in the simplest way possible. After all, not all problems require the most complicated solutions.

**Day 6 == Done!**
