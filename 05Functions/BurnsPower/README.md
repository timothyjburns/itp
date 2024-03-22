# Power

## What I Did

- Started with "def print_graph(n):" prompt. With inspiration from the Function Exercises in class repository, I wrote this piece of code for that function:

```
def print_graph(n):
    for i in range(n):
        print("*", end='')
        print('')
```
*PROBLEM* It prints a line after each asterisk, not at the end of the sequence.

*SOLUTION* INDENTATION IS IMPORTANT. I changed it to look like this, and added a prompt for n:

```
def print_graph(n):
    for i in range(n):
        print("*", end='')
    print('')

n = int(input("Enter an integer number: "))
print_graph(n)
```

- for the "get_power(x, n)" function, I started with this:

```
def get_power(x, n):
    return x ** n
```

- I combined them all together to make:

```
def get_power(x, n):
    return x ** n

def print_graph(n):
    for i in range(-8, 9):
        get_power(i, n)
        print("*", end='')
    print('')

n = int(input("Enter an integer number: "))
print_graph(n)
```

*PROBLEM* It just prints The number of asterisks equal to the range of i, and doesn't utilise the get_power function.

*SOLUTION* I changed the first "print" line to print("*" * get_power(i, n), end='')

*PROBLEM* It prints all the asterisks on one line.

*SOLUTION* Get rid of the "end=''" part!

- It's working, it's working!
