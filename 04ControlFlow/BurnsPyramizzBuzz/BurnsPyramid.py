stacks = int(input("How many floors should the pyramid have?"))
if stacks < 1 or stacks > 8:
    print("That's a bad pyramid. Reconsider your actions. Goodbye.")
else:
    for i in range(stacks):
        for j in range(stacks - 1 - i):
            print(' ', end='')
        for j in range(i + 1):
            print('#', end='')
        print()