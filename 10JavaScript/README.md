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
