# Pyramid / FizzBuzz

## Pyramid

### What I Did

- Tested the "square" example from the homework assignment to understand the concept

- First I'm trying to define the variable "stacks" with this code:

```
stacks = int(input("How many floors should the pyramid have?"))
if stacks < 0 or stacks > 8:
    print("That's a bad pyramid. Reconsider your actions. Goodbye.")
```
This seemed to work for values outside of the range, but thus far (obviously) nothing happens for values inside the range

- Using the idea of the square example, I wrote this code:

```
for i in range(stacks):
  for j in range(i - 1):
    print('#', end='')
  print()
```
*PROBLEM* It leaves too much space at the top of the pyramid.

*SOLUTION* Switched (i - 1) to (i + 1).

*PROBLEM* The pyramid is the wrong way around.

Next try was range(stacks - i), which flipped the pyramid over the x axis when I want to flip over the y axis.

THEN I realised that I want two different processes: one that affects the number of spaces and one that affects the number of #'s.

*SOLUTION* Added these two lines of code before the first "for j" function:

```
for j in range(stacks - i):
    print(' ', end='')
```

- I wanted to remove the offset from the entire pyramid, so I changed the j line of code to range(stacks - 1 - i)
