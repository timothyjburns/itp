# Chessboard

## What I Did

- Started in Python to understand the process better.

- Created a variable based on user input: ```
size = int(input("What size should the chessboard be?"))```

- I know it needs a nested loop so I looked up the pyramid assignment for inspiration

- A different process needs to happen depending on whether the sum of the row & column numbers is odd or even

- Created a blank string called "row", and this nested loop:

```
for i in range(size):
    row = ''
    for j in range(size):
        row += '#' if (i + j) % 2 == 0 else ' '
    print(row)
```
- Started in JavaScript, had to Google the function that returns an integer from the user input ("parseInt")

- The JavaScript equivalent of ```for i in range()``` is ```for (let i = 0, i < size, i++)```

- JavaScript is waaaay more complicated (right now at least, because I'm used to Python) when it comes to syntax. There were lots of typos with curly brackets and semi-colons in the wrong place, so I needed to go through the code very carefully to correct them all.

For example, I had the "console(log)" function inside a curly bracket loop and had to take it out for the nested loop to work properly. It seems that curly brackets have more power than indentation in JavaScript.
