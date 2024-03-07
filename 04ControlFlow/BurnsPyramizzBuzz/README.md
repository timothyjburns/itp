# Pyramid / FizzBuzz

## Pyramid

### What I Did

- Tested the "square" example from the homework assignment to understand the concept

- First I'm trying to define the variable "stacks" with this code:

```
stacks = int(input("How many floors should the pyramid have?"))
if stacks < 1 or stacks > 8:
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

## FizzBuzz

- This one makes more sense because of the work we've done so far in class. My first attempt was:

```
for i in range(1,100):
    if i % 3 == 0:
        print('Fizz')
    if i % 5 == 0:
        print('Buzz')
    print(i)
```

*PROBLEM* The program prints both the integer and Fizz/Buzz - I only want the FizzBuzz.

*SOLUTION* I added an "else" before the "print(i)".

*PROBLEM* The integer "100" is not printed.

*SOLUTION* Changed the range to (1,101).

*PROBLEM* For the multiples of both 3 & 5, "Fizz" and "Buzz" are printed on different lines.

*SOLUTION* Fixed that with a couple of "elif"s and a reordering. The end result is:

```
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)
```
