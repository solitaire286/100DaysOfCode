## Topics covered

- Random Module
- Understanding the Offset and Appending Items to Lists
- IndexErrors and Working with Nested Lists

## Notes

- Mersenne Twister is the pseudorandom number generator used in Python.
- Khan Academy video on pseudorandom number generators. [here](https://www.khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators)
- AskPython documentation on the Random module. [here](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences)
- A python module is, a file containing a set of functions you want to include in your application.
- Python documentation on Datastructures. [here](https://docs.python.org/3.10/tutorial/datastructures.html)
- Lists are used to store multiple items in a single variable.
- List items are ordered, changeable, and allow duplicate values.
- List items are indexed, the first item has index [0], the second item has index [1] etc. (Negative index [-1] start counting from last item to first.)
- Modify/Update a selected list item. e.g. brand_name = ["Apple", "Samsung", "Xiaomi"] => brand_name[2] = "Poco" // This will replace "Xiaomi" with "Poco".
- Append (Add) new item to list. e.g. brand_name.append("Vivo")
- Extend the list by adding multiple items. e.g. brand_name.extend(["Google", "OnePlus"]) (These items will be added to the end of the already existing list in the same name.)
- AskPython documentation on how to convert String to a List. [here](https://www.askpython.com/python/string/convert-string-to-list-in-python)
- Split string method is used to convert a string to list containing the constituent strings of the parent string (previously separated by some separator like ‘,’ or space).

  e.g. Input = Bruce, Clark, Diana, Oliver => names.split(", ") => ['Bruce', 'Clark', 'Diana', 'Oliver']

  Note: By default, if we do not pass anything to the split() method it splits up the string on the basis of the position of spaces.

- Error: Index out of range. To access the last item, you use the index value of -1. To acces the second to last item, you use the index value of -2. e.g. print(names[names_count - 1])

## Exercise & Project

- Heads or Tails
- Banker Roulette: Who will pay the bill?
- Treasure Map
- Rock Paper Scissors

## Thoughts

Completing day 4 took too long due to some ongoing life and work commitments. It felt frustrating, for each day I was unable to finish the assignments intending to move on.

It took going over some of my previous exercises and notes to get a refresh on everything I've covered so far, but it really helped me get back to speed.

And I realized how important it is to take notes while learning, even if it's just a single line description or an example snippet of code. Because at times I wonder if I'm spending too much time in summarizing and writing notes, which is time I could be writing code instead.

The "Rock, Paper, Scissors" project was interesting. I was able to complete it by myself with help of my notes and a bit of googling. That helped me regain some of the confidence I lost in days I was unable to do much.

It was nice knowing the steps in my codebase were quite similar to Angela's solution, and I had actually given it a bit of "personality" in my own way.

I cannot promise to myself or anyone that there will not be any more delays. After all, life happens. But I will continue to keep getting back up and moving forward.

Day 4 == Done!
